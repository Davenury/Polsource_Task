create_note_table = '''
CREATE TABLE IF NOT EXISTS Notes (
    title text NOT NULL,
    content text NOT NULL,
    created timestamp ,
    modified timestamp ,
    version integer,
    deleted boolean
);
'''

create_note_version_table = '''
CREATE TABLE IF NOT EXISTS Note_version(
    note_id integer not null,
    title text not null,
    content text not null,
    created timestamp,
    modified timestamp,
    version integer,
    deleted boolean,
    FOREIGN KEY (note_id) REFERENCES Notes (ROWID)
);
'''
