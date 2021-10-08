# FieldValue

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**field_name** | **str** | The name of the field. | [optional] 
**values** | **list[dict(str, object)]** | The values assigned to the field. | [optional] 
**field_type** | **OneOfFieldValueFieldType** | The type of the field. The possible field types are listed below. | [optional] 
**group_id** | **int** | The group id of the multi value field group. If the field is not a part of a multi value field group, then there is no group id. | [optional] 
**field_id** | **int** | The ID of the field. | [optional] 
**is_multi_value** | **bool** | A boolean indicating if the represented field supports multiple values. | [optional] 
**is_required** | **bool** | A boolean indicating if the represented field must have a value set on entries assigned to a template that the field is a member of. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

