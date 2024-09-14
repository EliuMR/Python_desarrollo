#Crear database
create database if not exists aplicacion_python;
use aplicacion_python;

create table if not exists usuarios(
                id              int(25)         auto_increment not null,
                nombre          varchar(100)    not null,
                apellidos       varchar(255),
                email           varchar(255)    not null,
                password        varchar(255)    not null,
                fecha           date            not null,
                constraint      pk_usuarios     primary key(id),
                constraint      uq_email        unique(email)
                )engine=InnoDb;

create table if not exists notas(
                id              int(25)         not null auto_increment,
                usuario_id      int(25)         not null,
                titulo          varchar(255)    not null,
                descripcion     varchar(255),
                fecha           date            not null,
                constraint      pk_notas        primary key(id),
                constraint      fk_notas_usuarios foreign key(usuario_id)       references usuarios(id)
                )engine=InnoDb;
