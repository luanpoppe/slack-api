from dataclasses import dataclass
from typing import Dict, Literal
from pydantic import BaseModel

from src.domain.slack.forms.form_input_value import FormInputValue


class CreateNewProjectForm(BaseModel):
    project_name_block: Dict[Literal["project_name_input"], FormInputValue]
    project_description_block: Dict[
        Literal["project_description_input"], FormInputValue
    ]
    form_question_block1: Dict[Literal["form_question_input1"], FormInputValue]
    form_question_block2: Dict[Literal["form_question_input2"], FormInputValue]
    form_question_block3: Dict[Literal["form_question_input3"], FormInputValue]

    def get_values(self):
        return CreateNewProjectFormFormated(
            name=self.project_name_block["project_name_input"].value,
            description=self.project_description_block[
                "project_description_input"
            ].value,
            question_1=self.form_question_block1["form_question_input1"].value,
            question_2=self.form_question_block2["form_question_input2"].value,
            question_3=self.form_question_block3["form_question_input3"].value,
        )


@dataclass
class CreateNewProjectFormFormated:
    name: str
    description: str
    question_1: str
    question_2: str
    question_3: str
