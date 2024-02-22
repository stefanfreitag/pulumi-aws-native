// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package devicefarm

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS::DeviceFarm::TestGridProject creates a new TestGrid Project
type TestGridProject struct {
	pulumi.CustomResourceState

	Arn         pulumi.StringOutput               `pulumi:"arn"`
	Description pulumi.StringPtrOutput            `pulumi:"description"`
	Name        pulumi.StringOutput               `pulumi:"name"`
	Tags        aws.TagArrayOutput                `pulumi:"tags"`
	VpcConfig   TestGridProjectVpcConfigPtrOutput `pulumi:"vpcConfig"`
}

// NewTestGridProject registers a new resource with the given unique name, arguments, and options.
func NewTestGridProject(ctx *pulumi.Context,
	name string, args *TestGridProjectArgs, opts ...pulumi.ResourceOption) (*TestGridProject, error) {
	if args == nil {
		args = &TestGridProjectArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource TestGridProject
	err := ctx.RegisterResource("aws-native:devicefarm:TestGridProject", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTestGridProject gets an existing TestGridProject resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTestGridProject(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TestGridProjectState, opts ...pulumi.ResourceOption) (*TestGridProject, error) {
	var resource TestGridProject
	err := ctx.ReadResource("aws-native:devicefarm:TestGridProject", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering TestGridProject resources.
type testGridProjectState struct {
}

type TestGridProjectState struct {
}

func (TestGridProjectState) ElementType() reflect.Type {
	return reflect.TypeOf((*testGridProjectState)(nil)).Elem()
}

type testGridProjectArgs struct {
	Description *string                   `pulumi:"description"`
	Name        *string                   `pulumi:"name"`
	Tags        []aws.Tag                 `pulumi:"tags"`
	VpcConfig   *TestGridProjectVpcConfig `pulumi:"vpcConfig"`
}

// The set of arguments for constructing a TestGridProject resource.
type TestGridProjectArgs struct {
	Description pulumi.StringPtrInput
	Name        pulumi.StringPtrInput
	Tags        aws.TagArrayInput
	VpcConfig   TestGridProjectVpcConfigPtrInput
}

func (TestGridProjectArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*testGridProjectArgs)(nil)).Elem()
}

type TestGridProjectInput interface {
	pulumi.Input

	ToTestGridProjectOutput() TestGridProjectOutput
	ToTestGridProjectOutputWithContext(ctx context.Context) TestGridProjectOutput
}

func (*TestGridProject) ElementType() reflect.Type {
	return reflect.TypeOf((**TestGridProject)(nil)).Elem()
}

func (i *TestGridProject) ToTestGridProjectOutput() TestGridProjectOutput {
	return i.ToTestGridProjectOutputWithContext(context.Background())
}

func (i *TestGridProject) ToTestGridProjectOutputWithContext(ctx context.Context) TestGridProjectOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TestGridProjectOutput)
}

type TestGridProjectOutput struct{ *pulumi.OutputState }

func (TestGridProjectOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**TestGridProject)(nil)).Elem()
}

func (o TestGridProjectOutput) ToTestGridProjectOutput() TestGridProjectOutput {
	return o
}

func (o TestGridProjectOutput) ToTestGridProjectOutputWithContext(ctx context.Context) TestGridProjectOutput {
	return o
}

func (o TestGridProjectOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *TestGridProject) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o TestGridProjectOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *TestGridProject) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o TestGridProjectOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *TestGridProject) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

func (o TestGridProjectOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *TestGridProject) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o TestGridProjectOutput) VpcConfig() TestGridProjectVpcConfigPtrOutput {
	return o.ApplyT(func(v *TestGridProject) TestGridProjectVpcConfigPtrOutput { return v.VpcConfig }).(TestGridProjectVpcConfigPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TestGridProjectInput)(nil)).Elem(), &TestGridProject{})
	pulumi.RegisterOutputType(TestGridProjectOutput{})
}
