route_schema = {
    "type": "object",
    "properties": {
        "route": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "step": {"type": "integer"},
                    "department": {"type": "string", "format": "uuid"},
                    "role_type": {"type": "string"},
                    "need_document": {"type": "boolean"},
                    "id_template_document": {"type": "string", "format": "uuid"},
                },
                "required": ["step", "department", "need_document", "role_type"],
            },
        },
    },
    "required": ["route"],
}
