# Parallelism and Asynchrony
## IO-bound. Проверяем ссылки на страницах Википедии
1. Время синхронной проверки ссылок
![sync_link.png](sync_link.png)
2. 5 воркеров
![img.png](5work.png) ![](OC 5 work.png)
3. 10 воркеров
![10work](10work.png)![](OC 10 work.png)
4. 100 воркеров
![img.png](100 work.png)![img.png](OC 100 work.png)
5. Количество воркеров влияет на критично загрузку памяти, ЦП держится на одном уровне (11% на 100 воркерах -скачок), 
время работы уменьшается при большем количестве воркеров.

## CPU-bound. Генерируем монетки
1. 2 Воркера, 22% ЦП ![img.png](2work_CPU_Bound.png)
2. 4 Воркера, 45% ЦП ![img.png](4work_CPU_Bound.png)
3. 5 Воркеров, 55% ЦП ![img.png](5work_CPU_Bound.png)
4. 10 Воркеров, 98% ЦП ![img.png](10work_CPU_Bound.png)
5. 100 Воркеров, 99% ЦП ![img.png](100work_CPU_Bound.png)

При большем количестве воркеров нагрузка на ЦП повышалась, но система не давала 100% загрузку ЦП.

На скриншотах видно, что при 100 воркерах программа завершилась позже, чем при 10. Всё за количества процессов, их очень много
и ЦП тратит время на передачу задач исполнения от одного процесса к другому.