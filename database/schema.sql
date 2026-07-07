-- Engineering Intelligence Platform MVP schema

create table if not exists projects (
    id uuid primary key default gen_random_uuid(),
    name text not null,
    created_at timestamptz not null default now()
);

create table if not exists documents (
    id uuid primary key default gen_random_uuid(),
    project_id uuid references projects(id),
    filename text not null,
    document_type text,
    revision text,
    created_at timestamptz not null default now()
);

create table if not exists document_pages (
    id uuid primary key default gen_random_uuid(),
    document_id uuid references documents(id),
    page_number int not null,
    page_type text not null,
    width numeric,
    height numeric,
    confidence numeric
);

create table if not exists engineering_objects (
    id uuid primary key default gen_random_uuid(),
    project_id uuid references projects(id),
    document_id uuid references documents(id),
    page_number int,
    tag text,
    object_type text not null,
    source_profile text not null default 'pid',
    x numeric,
    y numeric,
    width numeric,
    height numeric,
    confidence numeric,
    created_at timestamptz not null default now()
);

create table if not exists engineering_relationships (
    id uuid primary key default gen_random_uuid(),
    project_id uuid references projects(id),
    from_object_id uuid references engineering_objects(id),
    to_object_id uuid references engineering_objects(id),
    relationship_type text not null,
    confidence numeric,
    created_at timestamptz not null default now()
);

create table if not exists component_register_items (
    id uuid primary key default gen_random_uuid(),
    project_id uuid references projects(id),
    source_file text,
    source_sheet text,
    source_row int,
    tag text,
    description text,
    equipment_type text,
    system text,
    location text,
    maintenance_id text,
    raw_data jsonb,
    created_at timestamptz not null default now()
);
