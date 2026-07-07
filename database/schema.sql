-- Engineering Intelligence Platform initial schema

create table if not exists documents (
    id uuid primary key,
    filename text not null,
    document_type text,
    revision text,
    uploaded_at timestamptz default now()
);

create table if not exists pages (
    id uuid primary key,
    document_id uuid references documents(id),
    page_number integer not null,
    page_type text not null,
    confidence numeric not null default 0,
    metadata jsonb not null default '{}'::jsonb
);

create table if not exists symbols (
    id uuid primary key,
    document_id uuid references documents(id),
    page_number integer,
    symbol_type text not null,
    label text,
    bbox jsonb,
    source text,
    confidence numeric not null default 0
);

create table if not exists components (
    id uuid primary key,
    document_id uuid references documents(id),
    tag text,
    component_type text not null,
    page_number integer,
    bbox jsonb,
    properties jsonb not null default '{}'::jsonb,
    confidence numeric not null default 0,
    source text
);

create table if not exists relationships (
    id uuid primary key,
    source_component_id uuid references components(id),
    target_component_id uuid references components(id),
    relationship_type text not null,
    properties jsonb not null default '{}'::jsonb,
    confidence numeric not null default 0,
    source text
);

create table if not exists component_register_items (
    id uuid primary key,
    external_id text,
    tag text,
    description text,
    component_type text,
    system text,
    location text,
    source_file text,
    source_row integer,
    properties jsonb not null default '{}'::jsonb
);

create table if not exists component_matches (
    id uuid primary key,
    component_id uuid references components(id),
    register_item_id uuid references component_register_items(id),
    match_status text not null,
    confidence numeric not null default 0,
    reviewed boolean not null default false
);
