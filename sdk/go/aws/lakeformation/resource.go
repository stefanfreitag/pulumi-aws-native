// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package lakeformation

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::LakeFormation::Resource
//
// Deprecated: Resource is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Resource struct {
	pulumi.CustomResourceState

	ResourceArn          pulumi.StringOutput    `pulumi:"resourceArn"`
	RoleArn              pulumi.StringPtrOutput `pulumi:"roleArn"`
	UseServiceLinkedRole pulumi.BoolOutput      `pulumi:"useServiceLinkedRole"`
	WithFederation       pulumi.BoolPtrOutput   `pulumi:"withFederation"`
}

// NewResource registers a new resource with the given unique name, arguments, and options.
func NewResource(ctx *pulumi.Context,
	name string, args *ResourceArgs, opts ...pulumi.ResourceOption) (*Resource, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ResourceArn == nil {
		return nil, errors.New("invalid value for required argument 'ResourceArn'")
	}
	if args.UseServiceLinkedRole == nil {
		return nil, errors.New("invalid value for required argument 'UseServiceLinkedRole'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"resourceArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Resource
	err := ctx.RegisterResource("aws-native:lakeformation:Resource", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResource gets an existing Resource resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResource(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourceState, opts ...pulumi.ResourceOption) (*Resource, error) {
	var resource Resource
	err := ctx.ReadResource("aws-native:lakeformation:Resource", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Resource resources.
type resourceState struct {
}

type ResourceState struct {
}

func (ResourceState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceState)(nil)).Elem()
}

type resourceArgs struct {
	ResourceArn          string  `pulumi:"resourceArn"`
	RoleArn              *string `pulumi:"roleArn"`
	UseServiceLinkedRole bool    `pulumi:"useServiceLinkedRole"`
	WithFederation       *bool   `pulumi:"withFederation"`
}

// The set of arguments for constructing a Resource resource.
type ResourceArgs struct {
	ResourceArn          pulumi.StringInput
	RoleArn              pulumi.StringPtrInput
	UseServiceLinkedRole pulumi.BoolInput
	WithFederation       pulumi.BoolPtrInput
}

func (ResourceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourceArgs)(nil)).Elem()
}

type ResourceInput interface {
	pulumi.Input

	ToResourceOutput() ResourceOutput
	ToResourceOutputWithContext(ctx context.Context) ResourceOutput
}

func (*Resource) ElementType() reflect.Type {
	return reflect.TypeOf((**Resource)(nil)).Elem()
}

func (i *Resource) ToResourceOutput() ResourceOutput {
	return i.ToResourceOutputWithContext(context.Background())
}

func (i *Resource) ToResourceOutputWithContext(ctx context.Context) ResourceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResourceOutput)
}

func (i *Resource) ToOutput(ctx context.Context) pulumix.Output[*Resource] {
	return pulumix.Output[*Resource]{
		OutputState: i.ToResourceOutputWithContext(ctx).OutputState,
	}
}

type ResourceOutput struct{ *pulumi.OutputState }

func (ResourceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Resource)(nil)).Elem()
}

func (o ResourceOutput) ToResourceOutput() ResourceOutput {
	return o
}

func (o ResourceOutput) ToResourceOutputWithContext(ctx context.Context) ResourceOutput {
	return o
}

func (o ResourceOutput) ToOutput(ctx context.Context) pulumix.Output[*Resource] {
	return pulumix.Output[*Resource]{
		OutputState: o.OutputState,
	}
}

func (o ResourceOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Resource) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

func (o ResourceOutput) RoleArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Resource) pulumi.StringPtrOutput { return v.RoleArn }).(pulumi.StringPtrOutput)
}

func (o ResourceOutput) UseServiceLinkedRole() pulumi.BoolOutput {
	return o.ApplyT(func(v *Resource) pulumi.BoolOutput { return v.UseServiceLinkedRole }).(pulumi.BoolOutput)
}

func (o ResourceOutput) WithFederation() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *Resource) pulumi.BoolPtrOutput { return v.WithFederation }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResourceInput)(nil)).Elem(), &Resource{})
	pulumi.RegisterOutputType(ResourceOutput{})
}
