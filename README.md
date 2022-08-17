# json-restruct

Restruct JSON/Dict objects in Python.

### Warning
It is not production ready yet:) Written just for fun

### Features
- Flatten json
- Unflatten json
- Resturct json

### Usage
```python
user = {
    "full_name": "Adam Smith",
    "first_name": "Adam",
    "middle_name": "M",
    "last_name": "Smith",
    "lang": ["RU", "EN"],
    "extra": [
        {"facebook": 'www'}
    ],
    "hobbies": ["Music", "Sport"],
    "jobs": [
        {"company": "Apple", "positions": ["CEO"]},
        {"company": "GazOil", "positions": ["HR"]},
    ],
}

from json_restruct import flatten, unflatten, restruct

flatten_user = flatten(user)
print(flatten_user)

unflatten_user = unflatten(flatten_user)
print(unflatten_user)

restructure_map = {
    "full_name": "bio.full_name",
    "first_name": "bio.first_name",
    "middle_name": "bio.middle_name",
    "last_name": "bio.last_name",
    "lang": "languages.0.known.0.uni",
    "hobbies": "interests",
    "jobs.{}.company": "work.{}.company.name",
    "extra.{}.facebook": "facebook",
}

new_user = restruct(user, restructure_map)
```

Now, new_user looks like this
```json
{
  "work": [
    {
      "company": {
        "name": "Apple"
      }
    }
  ],
  "interests": [
    "Music",
    "Sport"
  ],
  "facebook": "www",
  "languages": [
    {
      "known": [
        {
          "uni": [
            "RU",
            "EN"
          ]
        }
      ]
    }
  ],
  "bio": {
    "last_name": "Smith",
    "middle_name": "M",
    "first_name": "Adam",
    "full_name": "Adam Smith"
  }
}
```

### TODO

- [ ] Write Unit tests


