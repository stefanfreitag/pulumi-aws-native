// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package greengrass

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::Greengrass::SubscriptionDefinition
//
// Deprecated: SubscriptionDefinition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type SubscriptionDefinition struct {
	pulumi.CustomResourceState

	Arn              pulumi.StringOutput                        `pulumi:"arn"`
	InitialVersion   SubscriptionDefinitionVersionTypePtrOutput `pulumi:"initialVersion"`
	LatestVersionArn pulumi.StringOutput                        `pulumi:"latestVersionArn"`
	Name             pulumi.StringOutput                        `pulumi:"name"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Greengrass::SubscriptionDefinition` for more information about the expected schema for this property.
	Tags pulumi.AnyOutput `pulumi:"tags"`
}

// NewSubscriptionDefinition registers a new resource with the given unique name, arguments, and options.
func NewSubscriptionDefinition(ctx *pulumi.Context,
	name string, args *SubscriptionDefinitionArgs, opts ...pulumi.ResourceOption) (*SubscriptionDefinition, error) {
	if args == nil {
		args = &SubscriptionDefinitionArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"initialVersion",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource SubscriptionDefinition
	err := ctx.RegisterResource("aws-native:greengrass:SubscriptionDefinition", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSubscriptionDefinition gets an existing SubscriptionDefinition resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSubscriptionDefinition(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SubscriptionDefinitionState, opts ...pulumi.ResourceOption) (*SubscriptionDefinition, error) {
	var resource SubscriptionDefinition
	err := ctx.ReadResource("aws-native:greengrass:SubscriptionDefinition", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SubscriptionDefinition resources.
type subscriptionDefinitionState struct {
}

type SubscriptionDefinitionState struct {
}

func (SubscriptionDefinitionState) ElementType() reflect.Type {
	return reflect.TypeOf((*subscriptionDefinitionState)(nil)).Elem()
}

type subscriptionDefinitionArgs struct {
	InitialVersion *SubscriptionDefinitionVersionType `pulumi:"initialVersion"`
	Name           *string                            `pulumi:"name"`
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Greengrass::SubscriptionDefinition` for more information about the expected schema for this property.
	Tags interface{} `pulumi:"tags"`
}

// The set of arguments for constructing a SubscriptionDefinition resource.
type SubscriptionDefinitionArgs struct {
	InitialVersion SubscriptionDefinitionVersionTypePtrInput
	Name           pulumi.StringPtrInput
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Greengrass::SubscriptionDefinition` for more information about the expected schema for this property.
	Tags pulumi.Input
}

func (SubscriptionDefinitionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*subscriptionDefinitionArgs)(nil)).Elem()
}

type SubscriptionDefinitionInput interface {
	pulumi.Input

	ToSubscriptionDefinitionOutput() SubscriptionDefinitionOutput
	ToSubscriptionDefinitionOutputWithContext(ctx context.Context) SubscriptionDefinitionOutput
}

func (*SubscriptionDefinition) ElementType() reflect.Type {
	return reflect.TypeOf((**SubscriptionDefinition)(nil)).Elem()
}

func (i *SubscriptionDefinition) ToSubscriptionDefinitionOutput() SubscriptionDefinitionOutput {
	return i.ToSubscriptionDefinitionOutputWithContext(context.Background())
}

func (i *SubscriptionDefinition) ToSubscriptionDefinitionOutputWithContext(ctx context.Context) SubscriptionDefinitionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SubscriptionDefinitionOutput)
}

type SubscriptionDefinitionOutput struct{ *pulumi.OutputState }

func (SubscriptionDefinitionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SubscriptionDefinition)(nil)).Elem()
}

func (o SubscriptionDefinitionOutput) ToSubscriptionDefinitionOutput() SubscriptionDefinitionOutput {
	return o
}

func (o SubscriptionDefinitionOutput) ToSubscriptionDefinitionOutputWithContext(ctx context.Context) SubscriptionDefinitionOutput {
	return o
}

func (o SubscriptionDefinitionOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *SubscriptionDefinition) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o SubscriptionDefinitionOutput) InitialVersion() SubscriptionDefinitionVersionTypePtrOutput {
	return o.ApplyT(func(v *SubscriptionDefinition) SubscriptionDefinitionVersionTypePtrOutput { return v.InitialVersion }).(SubscriptionDefinitionVersionTypePtrOutput)
}

func (o SubscriptionDefinitionOutput) LatestVersionArn() pulumi.StringOutput {
	return o.ApplyT(func(v *SubscriptionDefinition) pulumi.StringOutput { return v.LatestVersionArn }).(pulumi.StringOutput)
}

func (o SubscriptionDefinitionOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *SubscriptionDefinition) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Greengrass::SubscriptionDefinition` for more information about the expected schema for this property.
func (o SubscriptionDefinitionOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *SubscriptionDefinition) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SubscriptionDefinitionInput)(nil)).Elem(), &SubscriptionDefinition{})
	pulumi.RegisterOutputType(SubscriptionDefinitionOutput{})
}
