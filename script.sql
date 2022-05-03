CREATE TABLE IF NOT EXISTS public.users (
	"id" bigserial NOT NULL,
	"name" VARCHAR(100) NOT NULL,
	"document" VARCHAR(14) NOT NULL UNIQUE,
	CONSTRAINT users_pkey PRIMARY KEY (id)
);

CREATE table IF NOT EXISTS public.accounts (
	"id" bigserial NOT NULL PRIMARY key,
	"status" VARCHAR(6) NOT NULL CHECK("status" in ('ACTIVE', 'LOCKED', 'CLOSED')),
	"number" int4 NOT NULL,
	"bank_branch" TEXT NOT NULL CHECK( LENGTH("bank_branch") = 4 ),
	"balance" float8 NOT NULL,
	"withdraw_daily_limit" float8 NOT NULL,
	"user_id" bigserial NOT NULL,
	CONSTRAINT accounts_user_id_fk FOREIGN KEY ("user_id") REFERENCES public.users(id)
);

CREATE TABLE IF NOT EXISTS public.transactions (
	"id" bigserial NOT NULL PRIMARY KEY,
	"account_id" bigserial NOT NULL,
	"type" VARCHAR(8) NOT NULL CHECK("type" in ('WITHDRAW', 'DEPOSIT')),
	"value" float8 NOT NULL,
	"date" TIMESTAMP(4) NOT NULL,
	FOREIGN KEY("account_id") REFERENCES public.accounts("id")
);
