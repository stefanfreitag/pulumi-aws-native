// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package iottwinmaker

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource schema for AWS::IoTTwinMaker::ComponentType
type ComponentType struct {
	pulumi.CustomResourceState

	// The ARN of the component type.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The ID of the component type.
	ComponentTypeId pulumi.StringOutput `pulumi:"componentTypeId"`
	// An map of the composite component types in the component type. Each composite component type's key must be unique to this map.
	CompositeComponentTypes pulumi.AnyOutput `pulumi:"compositeComponentTypes"`
	// The date and time when the component type was created.
	CreationDateTime pulumi.StringOutput `pulumi:"creationDateTime"`
	// The description of the component type.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Specifies the parent component type to extend.
	ExtendsFrom pulumi.StringArrayOutput `pulumi:"extendsFrom"`
	// a Map of functions in the component type. Each function's key must be unique to this map.
	Functions pulumi.AnyOutput `pulumi:"functions"`
	// A Boolean value that specifies whether the component type is abstract.
	IsAbstract pulumi.BoolOutput `pulumi:"isAbstract"`
	// A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.
	IsSchemaInitialized pulumi.BoolOutput `pulumi:"isSchemaInitialized"`
	// A Boolean value that specifies whether an entity can have more than one component of this type.
	IsSingleton pulumi.BoolPtrOutput `pulumi:"isSingleton"`
	// An map of the property definitions in the component type. Each property definition's key must be unique to this map.
	PropertyDefinitions pulumi.AnyOutput `pulumi:"propertyDefinitions"`
	// An map of the property groups in the component type. Each property group's key must be unique to this map.
	PropertyGroups pulumi.AnyOutput `pulumi:"propertyGroups"`
	// The current status of the component type.
	Status ComponentTypeStatusOutput `pulumi:"status"`
	// A map of key-value pairs to associate with a resource.
	Tags pulumi.AnyOutput `pulumi:"tags"`
	// The last date and time when the component type was updated.
	UpdateDateTime pulumi.StringOutput `pulumi:"updateDateTime"`
	// The ID of the workspace that contains the component type.
	WorkspaceId pulumi.StringOutput `pulumi:"workspaceId"`
}

// NewComponentType registers a new resource with the given unique name, arguments, and options.
func NewComponentType(ctx *pulumi.Context,
	name string, args *ComponentTypeArgs, opts ...pulumi.ResourceOption) (*ComponentType, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ComponentTypeId == nil {
		return nil, errors.New("invalid value for required argument 'ComponentTypeId'")
	}
	if args.WorkspaceId == nil {
		return nil, errors.New("invalid value for required argument 'WorkspaceId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"componentTypeId",
		"workspaceId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ComponentType
	err := ctx.RegisterResource("aws-native:iottwinmaker:ComponentType", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetComponentType gets an existing ComponentType resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetComponentType(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ComponentTypeState, opts ...pulumi.ResourceOption) (*ComponentType, error) {
	var resource ComponentType
	err := ctx.ReadResource("aws-native:iottwinmaker:ComponentType", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ComponentType resources.
type componentTypeState struct {
}

type ComponentTypeState struct {
}

func (ComponentTypeState) ElementType() reflect.Type {
	return reflect.TypeOf((*componentTypeState)(nil)).Elem()
}

type componentTypeArgs struct {
	// The ID of the component type.
	ComponentTypeId string `pulumi:"componentTypeId"`
	// An map of the composite component types in the component type. Each composite component type's key must be unique to this map.
	CompositeComponentTypes interface{} `pulumi:"compositeComponentTypes"`
	// The description of the component type.
	Description *string `pulumi:"description"`
	// Specifies the parent component type to extend.
	ExtendsFrom []string `pulumi:"extendsFrom"`
	// a Map of functions in the component type. Each function's key must be unique to this map.
	Functions interface{} `pulumi:"functions"`
	// A Boolean value that specifies whether an entity can have more than one component of this type.
	IsSingleton *bool `pulumi:"isSingleton"`
	// An map of the property definitions in the component type. Each property definition's key must be unique to this map.
	PropertyDefinitions interface{} `pulumi:"propertyDefinitions"`
	// An map of the property groups in the component type. Each property group's key must be unique to this map.
	PropertyGroups interface{} `pulumi:"propertyGroups"`
	// A map of key-value pairs to associate with a resource.
	Tags interface{} `pulumi:"tags"`
	// The ID of the workspace that contains the component type.
	WorkspaceId string `pulumi:"workspaceId"`
}

// The set of arguments for constructing a ComponentType resource.
type ComponentTypeArgs struct {
	// The ID of the component type.
	ComponentTypeId pulumi.StringInput
	// An map of the composite component types in the component type. Each composite component type's key must be unique to this map.
	CompositeComponentTypes pulumi.Input
	// The description of the component type.
	Description pulumi.StringPtrInput
	// Specifies the parent component type to extend.
	ExtendsFrom pulumi.StringArrayInput
	// a Map of functions in the component type. Each function's key must be unique to this map.
	Functions pulumi.Input
	// A Boolean value that specifies whether an entity can have more than one component of this type.
	IsSingleton pulumi.BoolPtrInput
	// An map of the property definitions in the component type. Each property definition's key must be unique to this map.
	PropertyDefinitions pulumi.Input
	// An map of the property groups in the component type. Each property group's key must be unique to this map.
	PropertyGroups pulumi.Input
	// A map of key-value pairs to associate with a resource.
	Tags pulumi.Input
	// The ID of the workspace that contains the component type.
	WorkspaceId pulumi.StringInput
}

func (ComponentTypeArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*componentTypeArgs)(nil)).Elem()
}

type ComponentTypeInput interface {
	pulumi.Input

	ToComponentTypeOutput() ComponentTypeOutput
	ToComponentTypeOutputWithContext(ctx context.Context) ComponentTypeOutput
}

func (*ComponentType) ElementType() reflect.Type {
	return reflect.TypeOf((**ComponentType)(nil)).Elem()
}

func (i *ComponentType) ToComponentTypeOutput() ComponentTypeOutput {
	return i.ToComponentTypeOutputWithContext(context.Background())
}

func (i *ComponentType) ToComponentTypeOutputWithContext(ctx context.Context) ComponentTypeOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ComponentTypeOutput)
}

func (i *ComponentType) ToOutput(ctx context.Context) pulumix.Output[*ComponentType] {
	return pulumix.Output[*ComponentType]{
		OutputState: i.ToComponentTypeOutputWithContext(ctx).OutputState,
	}
}

type ComponentTypeOutput struct{ *pulumi.OutputState }

func (ComponentTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ComponentType)(nil)).Elem()
}

func (o ComponentTypeOutput) ToComponentTypeOutput() ComponentTypeOutput {
	return o
}

func (o ComponentTypeOutput) ToComponentTypeOutputWithContext(ctx context.Context) ComponentTypeOutput {
	return o
}

func (o ComponentTypeOutput) ToOutput(ctx context.Context) pulumix.Output[*ComponentType] {
	return pulumix.Output[*ComponentType]{
		OutputState: o.OutputState,
	}
}

// The ARN of the component type.
func (o ComponentTypeOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// The ID of the component type.
func (o ComponentTypeOutput) ComponentTypeId() pulumi.StringOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.StringOutput { return v.ComponentTypeId }).(pulumi.StringOutput)
}

// An map of the composite component types in the component type. Each composite component type's key must be unique to this map.
func (o ComponentTypeOutput) CompositeComponentTypes() pulumi.AnyOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.AnyOutput { return v.CompositeComponentTypes }).(pulumi.AnyOutput)
}

// The date and time when the component type was created.
func (o ComponentTypeOutput) CreationDateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.StringOutput { return v.CreationDateTime }).(pulumi.StringOutput)
}

// The description of the component type.
func (o ComponentTypeOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Specifies the parent component type to extend.
func (o ComponentTypeOutput) ExtendsFrom() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.StringArrayOutput { return v.ExtendsFrom }).(pulumi.StringArrayOutput)
}

// a Map of functions in the component type. Each function's key must be unique to this map.
func (o ComponentTypeOutput) Functions() pulumi.AnyOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.AnyOutput { return v.Functions }).(pulumi.AnyOutput)
}

// A Boolean value that specifies whether the component type is abstract.
func (o ComponentTypeOutput) IsAbstract() pulumi.BoolOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.BoolOutput { return v.IsAbstract }).(pulumi.BoolOutput)
}

// A Boolean value that specifies whether the component type has a schema initializer and that the schema initializer has run.
func (o ComponentTypeOutput) IsSchemaInitialized() pulumi.BoolOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.BoolOutput { return v.IsSchemaInitialized }).(pulumi.BoolOutput)
}

// A Boolean value that specifies whether an entity can have more than one component of this type.
func (o ComponentTypeOutput) IsSingleton() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.BoolPtrOutput { return v.IsSingleton }).(pulumi.BoolPtrOutput)
}

// An map of the property definitions in the component type. Each property definition's key must be unique to this map.
func (o ComponentTypeOutput) PropertyDefinitions() pulumi.AnyOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.AnyOutput { return v.PropertyDefinitions }).(pulumi.AnyOutput)
}

// An map of the property groups in the component type. Each property group's key must be unique to this map.
func (o ComponentTypeOutput) PropertyGroups() pulumi.AnyOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.AnyOutput { return v.PropertyGroups }).(pulumi.AnyOutput)
}

// The current status of the component type.
func (o ComponentTypeOutput) Status() ComponentTypeStatusOutput {
	return o.ApplyT(func(v *ComponentType) ComponentTypeStatusOutput { return v.Status }).(ComponentTypeStatusOutput)
}

// A map of key-value pairs to associate with a resource.
func (o ComponentTypeOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

// The last date and time when the component type was updated.
func (o ComponentTypeOutput) UpdateDateTime() pulumi.StringOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.StringOutput { return v.UpdateDateTime }).(pulumi.StringOutput)
}

// The ID of the workspace that contains the component type.
func (o ComponentTypeOutput) WorkspaceId() pulumi.StringOutput {
	return o.ApplyT(func(v *ComponentType) pulumi.StringOutput { return v.WorkspaceId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ComponentTypeInput)(nil)).Elem(), &ComponentType{})
	pulumi.RegisterOutputType(ComponentTypeOutput{})
}
