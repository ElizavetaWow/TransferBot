# TransferBot
Финальный проект для DLS
## О чём проект
Проект по созданию telegram-бота для переноса стиля одной фотографии на другую.

## Состав проекта
В качестве модели используется GAN [Multi-style Generative Network for Real-time Transfer](https://github.com/zhanghang1989/PyTorch-Multi-Style-Transfer). Полное описание модели [здесь](https://arxiv.org/pdf/1703.06953.pdf).
Архитектуру модели можно посмотреть в файле model.py, веса - в файле pretrained.model.

Telegram-бот написан с помощью асинхронного фреймворка aiogram. Ссылка на документацию: https://docs.aiogram.dev/en/latest/. 
Реализация в файле main.py. Токен бота вынесен в отдельный файл с названием token.txt. Все необходимые зависимости проекта находятся в requirements.txt.

Весь проект был упакован в докер.

Telegram-бот задеплоен на хостинге pythonanywhere (предупреждение: скорость работы ниже, чем при локальном запуске).

## Как использовать бота
1. Открыть бота в telegram @TransferImageStyleBot и нажать Старт.
2. Чтобы применить перенос стиля, нужно выбрать пункт Загрузить фото для обработки или написать /transfer. 
3. Следуя интрукциям бота, последовательно добавить фото для изменения и фото стиля.
4. Бот вернёт изменённое изображение.

Если на каком-то этапе Вы захотите прекратить работу с ботом - выберите пункт Отменить операцию или напишите /cancel.
Справку по доступным командам можно получить по кнопке Помощь или команде /help.

### Визуализация работы

<img src="https://lh3.googleusercontent.com/u/1/drive-viewer/AAOQEOTuumQkpiEuR85SGyoTDbNkW8uu7HQG8Ks3oIYCtjFnFc4N0WfGK3dkQjIv4ulXzJdW1S9duPJN9Lx4i_ysONCiBhVw5Q=w2488-h1231" width="200"><img src="https://user-images.githubusercontent.com/59148803/215332682-52cffb98-20d6-44d1-9fbf-bb6af60089e0.png" width="200"><img src="https://user-images.githubusercontent.com/59148803/215332194-79265d42-f35b-494a-adf5-63e5e2ae4ce9.png" width="200"><img src="https://lh3.googleusercontent.com/fife/AMPSemdaL9bdCrk8gr58okBhwJJIr-uWfOsUESlkIYVEI7t89fJcssk6V_ONMmwvdw8Oz6-8by-9AEZXlg4PuerQm0b-kf_88D35PZ0JZYT_N7005g_2-VBvnfMhi5WNUgqG6MMmAxCaX_k49uUKKkSN5eUz-Ogc89jvfEqfk8qmq-3NOm0EIQMhdJzkBqZQvG7jAxuLtcVFXLT46oqYeUi9Dx8pQf17UGGkThKX_h1cEBqQFsqXjJVrwVpVaYwyiNusjOYXn_-osxCOXN1RZ8UdZhyN8YDgbnOivlcpj8Us1RBZdGtU6Zswsnj8fEgz7urJQe6sZNr3EFkarD2xQo7kEuudxmQnI60CKBap2uByi5_qp6HboqLGBbaO8nljrjO8T12iSVB5Bsul2xlihIJqfwJkI0LpAO6zxT0kQaZgMKNOUXgf0ezRrzt_4Kau9qnNtMD5Eh8q4UsckMTagQpeTtQy6NBg0kXUPCerjXm0oC3pezBtZm_d3fWo5xhC3EsBqBOQ3ved8G470W5o3VGrgXkM5PRXfjARIpn3twk0jsFut-c967GcokOApHNYotMIMDr6XYr9T1i3eH-YsQxMJ3bmAdzTIOiHUUS0A2aEySzEvCNlkqq8bPdE_w359ql51qQo-yDGMiexooKCQ0vUcZzdT8veCKLyjnUKmqiHqca5fvxu-88gs69-qL6X2lnuYJaaXlpljwSXbBKaKwxydj78zEUZm9OX5LsE_0GzM5zWQd8l6qcIHMQIzkEkvtwQHtXs3wjJIyA1Der3hPcNNiPW8zebT89Vxl8dK9vUCycSOd8b1kOHz4x5rR1mm-tG_EoyetugD6XRFXuWrlrUdmoDUqx6bixffISdJcsIKwCdALUMsuj5acB08CjaLch2ylv5dDY6GamF_nl18BLKYU1sBhsRn3tqQk_IWaTBMMEfzgoIumI1DFrKSC7OoMWIA-DUY25fTQDdOd26hHl8BIDBkn6DID5j05WOP-Q6LlbfXgbYNJcgR38hR4DkJtD6clAjfrM4WHep6FAFzpUuUM5g4kNVzNmmaOAxOVaduDK6w5sRCH-j_NXbLvMPfJhMKZk3DK1jnqu06JSuKZyZkkUTQ9WS4aF0LBbLZ4SCNXwf7cb9_NIfEzsuKDwQSeb4CIzhLzZpEoINZiPZtc7ocsgjvgM9dQFi-fSzw1l1IB39bJaGTwe281JGQ4HNQZhp-4G-0t05keHT8w4NquB27h-5o78kzU7N04KRV5X6aM0U2R1sON_2xv9QDaCURhFIKQIkUxUB5c3FgnXpXB5FRURQRkVjbxdB4ias15WcweigDyxkdNz07rXfMQCNMN_To442Nrqf4zFN9__r9FaTsiZ6bPxGnz_rIWwCcfmHhXnm4wQSL8rypf2fpNSzXar6lGXtQz-c12eswWe00mRiJjj0uWjqZO_2Ibtf8WrJUZVfN3cIYIg90tQc6HKiycfKTIPMfoNt_sgIHFcx-rC4VBGvVaici7BfrboS5LbkfU6Zex6M-n2SrlohI4aKSFgWiVdkpTRQrQKXJXGm3LgSVIiNY9EKhQ=w2488-h1231" width="200">

### Примеры результатов
![MyCollages (3)](https://user-images.githubusercontent.com/59148803/215333814-fc047072-8c6b-4c33-b897-dec902b68daa.jpg)
