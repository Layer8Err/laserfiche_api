# WFieldInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the field. | [optional] 
**id** | **int** | The ID of the field. | [optional] 
**description** | **str** | The description of the field. | [optional] 
**field_type** | **OneOfWFieldInfoFieldType** | The type of the field. | [optional] 
**length** | **int** | The length of the field for variable length data types. | [optional] 
**default_value** | **str** | The default value of the field for new entries that are assigned to a template the represented field is a member of. | [optional] 
**is_multi_value** | **bool** | A boolean indicating if the represented template field supports multiple values. | [optional] 
**is_required** | **bool** | A boolean indicating if the represented field must have a value set on entries assigned to a template that the field is a member of. | [optional] 
**constraint** | **str** | The constraint for values stored in the represented field. | [optional] 
**constraint_error** | **str** | The error string that will be returned when the field constraint is violated when setting a value for this field. | [optional] 
**list_values** | **list[str]** | The list of items assigned to the represented field. | [optional] 
**format** | **OneOfWFieldInfoFormat** | The display format of the represented field. | [optional] 
**currency** | **str** | The name of the currency that will be using when formatting the represented field when the Format property is set to the Currency member of the WFieldFormat enumeration. | [optional] 
**format_pattern** | **str** | The custom format pattern for fields that are configured to use a custom format. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

