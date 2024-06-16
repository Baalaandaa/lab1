# Лабораторная работа 1

## Построение сети
Схема сети:

!['scheme'](./scheme.png)

Конфигурация каждого из устройств:

### VPC:
- Ставим pcname
- Назначаем адрес в сети, маску и gw
!['vpc config'](./vpc.png)

### SW1/2:
- Назначаем человеческое имя
- Объявляем vlan
- Настраиваем прокидку vlan в SW, SW2
- Настраиваем gi 0/2 чтобы создать vlan10
- Сохраняем конфиг 

!['sw12'](./sw1.png)

!['sw12'](./sw2.png)

### SW
- Назначаем человеческое имя
- Объявляем vlan
- Настраиваем прокидку vlan в SW1/2, R
- Назначаем vlan 10,20 корнем STP tree
- Сохраняем конфиг

!['sw'](./sw.png)

### R
- Назначаем человеческое имя
- Включаем gi 0/1
- Создаем 2 subif для разных vlan
- Сохраняем конфиг

!['R'](./R.png)

## Результат

!['stp_tree'](./vlan10st.png)

!['stp_tree'](./vlan20st.png)

Пинги:

!['pings'](./vpc1ping.png)

!['pings'](./vpc2ping.png)

### Эксперимент 1(SW -x> SW1):

!['s'](./exp1scheme.png)

!['s'](./exp1vpc1ping.png)

!['s'](./exp1vpc2ping.png)


### Эксперимент 2(SW1 <-x-> SW2):

!['s'](./exp2scheme.png)

!['s'](./exp2vpc1ping.png)

!['s'](./exp2vpc2ping.png)

### Эксперимент 3(SW -x> SW2):

!['s'](./exp3scheme.png)

!['s'](./exp3vpc1ping.png)

!['s'](./exp3vpc2ping.png)