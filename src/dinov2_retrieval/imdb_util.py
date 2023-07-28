#! /usr/bin/env python
# coding: utf-8

import lmdb


def initialize(db_dir, gb=1):
    env = lmdb.open(db_dir, map_size=1024 * 1024 * 1024 * gb)

    return env


def insert(env, key, value):
    txn = env.begin(write=True)
    txn.put(str(key).encode(), value)
    txn.commit()


def delete(env, key):
    txn = env.begin(write=True)
    txn.delete(str(key).encode())
    txn.commit()


def update(env, key, value):
    txn = env.begin(write=True)
    txn.put(str(key).encode(), value)
    txn.commit()


def get(env, key):
    txn = env.begin(write=False)
    value = txn.get(str(key).encode())
    return value


def traverse(env):
    txn = env.begin(write=False)
    for key, value in txn.cursor():
        yield key.decode(), value


def stat(env):
    txn = env.begin(write=False)

    return txn.stat()


def count(env):
    txn = env.begin(write=False)

    return txn.stat()["entries"]
