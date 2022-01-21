drop table public.transactions;
drop table public.accounts;
drop table public.users;

CREATE TABLE public.users (
	"id" bigserial NOT NULL,
	"name" varchar(100) NOT NULL,
	"document" varchar(14) NOT NULL UNIQUE,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);

CREATE table public.accounts (
	"id" bigserial not null PRIMARY key,
	"status" varchar(6) not null CHECK("status" in ('ACTIVE', 'LOCKED', 'CLOSED')),
	"number" int4 not null,
	"bank_branch" varchar(6) not null,
	"balance" float8 not null,
	"withdraw_daily_limit" float8 not null,
	"user_id" bigserial not null,
	CONSTRAINT accounts_user_id_fk FOREIGN KEY ("user_id") REFERENCES public.users(id)
);

CREATE TABLE public.transactions (
	"id" bigserial NOT NULL PRIMARY KEY,
	"account_id" bigserial NOT NULL,
	"type" varchar(8) NOT NULL CHECK("type" in ('WITHDRAW', 'DEPOSIT')),
	"value" float8 NOT NULL,
	"date" timestamp(4) NOT NULL,
	FOREIGN KEY("account_id") REFERENCES public.accounts("id")
);

insert into users (name, document) values ('Gabriel Leandro', '44697109899');
insert into accounts (
	number, 
	bankBranch, 
	balance, 
	userId, 
	status,
	withdrawDailyLimit) 
values (
	44609, 
	'0001',
	1.50,
	1,
	'ACTIVE',
	2000.00
);
