from dataclasses import dataclass


@dataclass
class ModalIdsEnum:
    create_new_project_id = "create_new_project_id"

    def answer_project_form_id(self, project_id: str):
        return f"answer_project_form_id_{project_id}"
