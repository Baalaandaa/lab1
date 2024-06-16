import click
import ipaddress
import socket
import icmplib

@click.command()
@click.argument('target', type=str, required=True)
@click.option('--lower', type=click.IntRange(0, 10_000_000), default=0, help='The lower bound of the MTU search')
@click.option('--upper', type=click.IntRange(0, 10_000_000), default=1_048_576, help='The upper bound of the MTU search')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose output')
@click.option('--count', '-c', type=click.IntRange(0, 100), default=3, help='Number of ping attempts per test')
@click.option('--interval', '-i', type=click.FloatRange(0, 5), default=0.1, help='Interval between pings within a test')
@click.option('--timeout', '-W', type=click.FloatRange(0, 5), default=1, help='Ping timeout in seconds')
def main(target, lower, upper, verbose, count, interval, timeout):
    try:
        ip = ipaddress.ip_address(target)
        print(f'{target} is an IPv{ip.version} address')
    except ValueError:
        print(f'{target} is not a valid IPv4 or IPv6 address')
        try:
            resolved_ip = socket.gethostbyname(target)
            print(f'{target} is resolved to {resolved_ip}')
        except socket.gaierror:
            print(f'{target} could not be resolved')
            exit(1)

    min_mtu = lower - 1
    max_mtu = upper + 1
    while min_mtu + 1 < max_mtu:
        mid_mtu = (min_mtu + max_mtu) // 2
        try:
            ping_result = icmplib.ping(
                target,
                count=count,
                interval=interval,
                timeout=timeout,
                payload_size=mid_mtu - 28,
            )
        except icmplib.exceptions.NameLookupError:
            print(f'Unable to resolve {target}')
            exit(1)
        except icmplib.exceptions.DestinationUnreachable:
            print(f'{target} is unreachable')
            exit(1)
        except Exception as e:
            print(f'Error during ping: {e}')
            exit(1)

        if verbose:
            print(f'Ping {mid_mtu} bytes: sent={ping_result.packets_sent} received={ping_result.packets_received} loss={ping_result.packet_loss}')

        if ping_result.is_alive and ping_result.packet_loss == 0:
            min_mtu = mid_mtu
        else:
            max_mtu = mid_mtu

    if min_mtu == lower - 1:
        print(f'{target} is unreachable')
    else:
        print(f'The minimum MTU is {min_mtu} bytes')

if __name__ == '__main__':
    main()
