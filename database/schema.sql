create table if not exists documents (
    id uuid primary key,
    filename text not null,
    content_type text,
    stored_path text not null,
    created_at timestamptz default now()
);

create table if not exists pages (
    id uuid primary key,
    document_id uuid references documents(id),
    page_number integer not null,
    page_type text not null,
    confidence numeric,
    reason text
);

create table if not exists components (
    id uuid primary key,
    document_id uuid references documents(id),
    tag text not null,
    component_type text not null,
    page_number integer,
    confidence numeric,
    source text,
    created_at timestamptz default now()
);

create table if not exists legend_items (
    id uuid primary key,
    document_id uuid references documents(id),
    name text not null,
    page_number integer,
    confidence numeric,
    source text
);
