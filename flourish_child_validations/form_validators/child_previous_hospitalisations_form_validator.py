from edc_constants.constants import YES, OTHER
from edc_form_validators import FormValidator


class ChildPreviousHospitalisationFormValidator(FormValidator):

    def clean(self):

        required_fields = ['hospitalized_count', 'aprox_date']

        for required in required_fields:
            self.required_if(YES, field='child_hospitalized',
                             field_required=required)

        self.validate_other_specify(field='name_hospital')

        self.validate_other_specify(field='reason_hospitalized')

        self.m2m_other_specify(OTHER, m2m_field='reason_hospitalized',
                               field_other='reason_hospitalized_other')

        self.m2m_other_specify('Surgical_reason',
                               m2m_field='reason_hospitalized',
                               field_other='surgical_reason')
