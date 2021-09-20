// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// This resource creates a Registry for authoring schemas as part of Glue Schema Registry.
type Registry struct {
	pulumi.CustomResourceState

	// Amazon Resource Name for the created Registry.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A description of the registry. If description is not provided, there will not be any default value for this.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark.  No whitespace.
	Name pulumi.StringOutput `pulumi:"name"`
	// List of tags to tag the Registry
	Tags RegistryTagArrayOutput `pulumi:"tags"`
}

// NewRegistry registers a new resource with the given unique name, arguments, and options.
func NewRegistry(ctx *pulumi.Context,
	name string, args *RegistryArgs, opts ...pulumi.ResourceOption) (*Registry, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource Registry
	err := ctx.RegisterResource("aws-native:glue:Registry", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRegistry gets an existing Registry resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRegistry(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RegistryState, opts ...pulumi.ResourceOption) (*Registry, error) {
	var resource Registry
	err := ctx.ReadResource("aws-native:glue:Registry", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Registry resources.
type registryState struct {
}

type RegistryState struct {
}

func (RegistryState) ElementType() reflect.Type {
	return reflect.TypeOf((*registryState)(nil)).Elem()
}

type registryArgs struct {
	// A description of the registry. If description is not provided, there will not be any default value for this.
	Description *string `pulumi:"description"`
	// Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark.  No whitespace.
	Name string `pulumi:"name"`
	// List of tags to tag the Registry
	Tags []RegistryTag `pulumi:"tags"`
}

// The set of arguments for constructing a Registry resource.
type RegistryArgs struct {
	// A description of the registry. If description is not provided, there will not be any default value for this.
	Description pulumi.StringPtrInput
	// Name of the registry to be created of max length of 255, and may only contain letters, numbers, hyphen, underscore, dollar sign, or hash mark.  No whitespace.
	Name pulumi.StringInput
	// List of tags to tag the Registry
	Tags RegistryTagArrayInput
}

func (RegistryArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*registryArgs)(nil)).Elem()
}

type RegistryInput interface {
	pulumi.Input

	ToRegistryOutput() RegistryOutput
	ToRegistryOutputWithContext(ctx context.Context) RegistryOutput
}

func (*Registry) ElementType() reflect.Type {
	return reflect.TypeOf((*Registry)(nil))
}

func (i *Registry) ToRegistryOutput() RegistryOutput {
	return i.ToRegistryOutputWithContext(context.Background())
}

func (i *Registry) ToRegistryOutputWithContext(ctx context.Context) RegistryOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RegistryOutput)
}

type RegistryOutput struct{ *pulumi.OutputState }

func (RegistryOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Registry)(nil))
}

func (o RegistryOutput) ToRegistryOutput() RegistryOutput {
	return o
}

func (o RegistryOutput) ToRegistryOutputWithContext(ctx context.Context) RegistryOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RegistryOutput{})
}
