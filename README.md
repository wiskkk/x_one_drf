# x_one_drf
1. users/:
    > register/ - create users\
    > login/ - login users\
    > logout/ - users logout\
    > change-password/ - change users password\
    > token-refresh/ - refresg users token\
    
2. management/:
    > users/ - users list\
    > users/<pk:int>/ - user profile\
    > categories/ - CRUD categories\
---
Every day at 6 am statistics (account balance) is sent to email

Use for that celery with redis
