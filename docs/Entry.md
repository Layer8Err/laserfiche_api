# Entry

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The ID of the entry. | [optional] 
**name** | **str** | The name of the entry. | [optional] 
**parent_id** | **int** | The ID of the parent entry. | [optional] 
**full_path** | **str** | The full path in the Laserfiche repository to the entry. | [optional] 
**folder_path** | **str** | The path in the Laserfiche repository to the parent folder. | [optional] 
**creator** | **str** | The name of the user that created this entry. | [optional] 
**creation_time** | **datetime** | The creation time of the entry. | [optional] 
**last_modified_time** | **datetime** | The last modification time of the entry. | [optional] 
**entry_type** | **OneOfEntryEntryType** | The type of the entry. | [optional] 
**is_container** | **bool** | A boolean indicating if this entry is a container object; it can have other entries as children. | [optional] 
**is_leaf** | **bool** | A boolean indicating if this entry is a leaf object; it cannot have other entries as children. | [optional] 
**template_name** | **str** | The name of the template assigned to this entry. | [optional] 
**template_id** | **int** | The id of the template assigned to this entry. | [optional] 
**template_field_names** | **list[str]** | The names of the fields assigned to the template assigned to this entry. | [optional] 
**volume_name** | **str** | The name of the volume that this entry is associated with. | [optional] 
**fields** | [**list[FieldValue]**](FieldValue.md) | The fields assigned to this entry. | [optional] 
**tags** | [**list[WTagInfo]**](WTagInfo.md) | The tags assigned to this entry. | [optional] 
**links** | [**list[WEntryLinkInfo]**](WEntryLinkInfo.md) | The links assigned to this entry. | [optional] 
**row_number** | **int** | Row number assigned to this entry in the listing. | [optional] 
**properties** | **dict(str, object)** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

