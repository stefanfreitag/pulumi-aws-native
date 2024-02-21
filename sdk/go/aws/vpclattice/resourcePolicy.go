// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vpclattice

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Retrieves information about the resource policy. The resource policy is an IAM policy created by AWS RAM on behalf of the resource owner when they share a resource.
type ResourcePolicy struct {
	pulumi.CustomResourceState

	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::VpcLattice::ResourcePolicy` for more information about the expected schema for this property.
	Policy      pulumi.AnyOutput    `pulumi:"policy"`
	ResourceArn pulumi.StringOutput `pulumi:"resourceArn"`
}

// NewResourcePolicy registers a new resource with the given unique name, arguments, and options.
func NewResourcePolicy(ctx *pulumi.Context,
	name string, args *ResourcePolicyArgs, opts ...pulumi.ResourceOption) (*ResourcePolicy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Policy == nil {
		return nil, errors.New("invalid value for required argument 'Policy'")
	}
	if args.ResourceArn == nil {
		return nil, errors.New("invalid value for required argument 'ResourceArn'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"resourceArn",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ResourcePolicy
	err := ctx.RegisterResource("aws-native:vpclattice:ResourcePolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetResourcePolicy gets an existing ResourcePolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetResourcePolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ResourcePolicyState, opts ...pulumi.ResourceOption) (*ResourcePolicy, error) {
	var resource ResourcePolicy
	err := ctx.ReadResource("aws-native:vpclattice:ResourcePolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ResourcePolicy resources.
type resourcePolicyState struct {
}

type ResourcePolicyState struct {
}

func (ResourcePolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*resourcePolicyState)(nil)).Elem()
}

type resourcePolicyArgs struct {
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::VpcLattice::ResourcePolicy` for more information about the expected schema for this property.
	Policy      interface{} `pulumi:"policy"`
	ResourceArn string      `pulumi:"resourceArn"`
}

// The set of arguments for constructing a ResourcePolicy resource.
type ResourcePolicyArgs struct {
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::VpcLattice::ResourcePolicy` for more information about the expected schema for this property.
	Policy      pulumi.Input
	ResourceArn pulumi.StringInput
}

func (ResourcePolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*resourcePolicyArgs)(nil)).Elem()
}

type ResourcePolicyInput interface {
	pulumi.Input

	ToResourcePolicyOutput() ResourcePolicyOutput
	ToResourcePolicyOutputWithContext(ctx context.Context) ResourcePolicyOutput
}

func (*ResourcePolicy) ElementType() reflect.Type {
	return reflect.TypeOf((**ResourcePolicy)(nil)).Elem()
}

func (i *ResourcePolicy) ToResourcePolicyOutput() ResourcePolicyOutput {
	return i.ToResourcePolicyOutputWithContext(context.Background())
}

func (i *ResourcePolicy) ToResourcePolicyOutputWithContext(ctx context.Context) ResourcePolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ResourcePolicyOutput)
}

type ResourcePolicyOutput struct{ *pulumi.OutputState }

func (ResourcePolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ResourcePolicy)(nil)).Elem()
}

func (o ResourcePolicyOutput) ToResourcePolicyOutput() ResourcePolicyOutput {
	return o
}

func (o ResourcePolicyOutput) ToResourcePolicyOutputWithContext(ctx context.Context) ResourcePolicyOutput {
	return o
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::VpcLattice::ResourcePolicy` for more information about the expected schema for this property.
func (o ResourcePolicyOutput) Policy() pulumi.AnyOutput {
	return o.ApplyT(func(v *ResourcePolicy) pulumi.AnyOutput { return v.Policy }).(pulumi.AnyOutput)
}

func (o ResourcePolicyOutput) ResourceArn() pulumi.StringOutput {
	return o.ApplyT(func(v *ResourcePolicy) pulumi.StringOutput { return v.ResourceArn }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ResourcePolicyInput)(nil)).Elem(), &ResourcePolicy{})
	pulumi.RegisterOutputType(ResourcePolicyOutput{})
}
