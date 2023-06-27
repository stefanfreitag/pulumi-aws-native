// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package organizations

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Policies in AWS Organizations enable you to manage different features of the AWS accounts in your organization.  You can use policies when all features are enabled in your organization.
type Policy struct {
	pulumi.CustomResourceState

	// ARN of the Policy
	Arn pulumi.StringOutput `pulumi:"arn"`
	// A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
	AwsManaged pulumi.BoolOutput `pulumi:"awsManaged"`
	// The Policy text content. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.
	Content pulumi.AnyOutput `pulumi:"content"`
	// Human readable description of the policy
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Name of the Policy
	Name pulumi.StringOutput `pulumi:"name"`
	// A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
	Tags PolicyTagArrayOutput `pulumi:"tags"`
	// List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to
	TargetIds pulumi.StringArrayOutput `pulumi:"targetIds"`
	// The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY
	Type PolicyTypeOutput `pulumi:"type"`
}

// NewPolicy registers a new resource with the given unique name, arguments, and options.
func NewPolicy(ctx *pulumi.Context,
	name string, args *PolicyArgs, opts ...pulumi.ResourceOption) (*Policy, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Content == nil {
		return nil, errors.New("invalid value for required argument 'Content'")
	}
	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	var resource Policy
	err := ctx.RegisterResource("aws-native:organizations:Policy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPolicy gets an existing Policy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PolicyState, opts ...pulumi.ResourceOption) (*Policy, error) {
	var resource Policy
	err := ctx.ReadResource("aws-native:organizations:Policy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Policy resources.
type policyState struct {
}

type PolicyState struct {
}

func (PolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*policyState)(nil)).Elem()
}

type policyArgs struct {
	// The Policy text content. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.
	Content interface{} `pulumi:"content"`
	// Human readable description of the policy
	Description *string `pulumi:"description"`
	// Name of the Policy
	Name *string `pulumi:"name"`
	// A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
	Tags []PolicyTag `pulumi:"tags"`
	// List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to
	TargetIds []string `pulumi:"targetIds"`
	// The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY
	Type PolicyType `pulumi:"type"`
}

// The set of arguments for constructing a Policy resource.
type PolicyArgs struct {
	// The Policy text content. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.
	Content pulumi.Input
	// Human readable description of the policy
	Description pulumi.StringPtrInput
	// Name of the Policy
	Name pulumi.StringPtrInput
	// A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
	Tags PolicyTagArrayInput
	// List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to
	TargetIds pulumi.StringArrayInput
	// The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY
	Type PolicyTypeInput
}

func (PolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*policyArgs)(nil)).Elem()
}

type PolicyInput interface {
	pulumi.Input

	ToPolicyOutput() PolicyOutput
	ToPolicyOutputWithContext(ctx context.Context) PolicyOutput
}

func (*Policy) ElementType() reflect.Type {
	return reflect.TypeOf((**Policy)(nil)).Elem()
}

func (i *Policy) ToPolicyOutput() PolicyOutput {
	return i.ToPolicyOutputWithContext(context.Background())
}

func (i *Policy) ToPolicyOutputWithContext(ctx context.Context) PolicyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PolicyOutput)
}

type PolicyOutput struct{ *pulumi.OutputState }

func (PolicyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Policy)(nil)).Elem()
}

func (o PolicyOutput) ToPolicyOutput() PolicyOutput {
	return o
}

func (o PolicyOutput) ToPolicyOutputWithContext(ctx context.Context) PolicyOutput {
	return o
}

// ARN of the Policy
func (o PolicyOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Policy) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// A boolean value that indicates whether the specified policy is an AWS managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.
func (o PolicyOutput) AwsManaged() pulumi.BoolOutput {
	return o.ApplyT(func(v *Policy) pulumi.BoolOutput { return v.AwsManaged }).(pulumi.BoolOutput)
}

// The Policy text content. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.
func (o PolicyOutput) Content() pulumi.AnyOutput {
	return o.ApplyT(func(v *Policy) pulumi.AnyOutput { return v.Content }).(pulumi.AnyOutput)
}

// Human readable description of the policy
func (o PolicyOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Policy) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// Name of the Policy
func (o PolicyOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Policy) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to null.
func (o PolicyOutput) Tags() PolicyTagArrayOutput {
	return o.ApplyT(func(v *Policy) PolicyTagArrayOutput { return v.Tags }).(PolicyTagArrayOutput)
}

// List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to
func (o PolicyOutput) TargetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Policy) pulumi.StringArrayOutput { return v.TargetIds }).(pulumi.StringArrayOutput)
}

// The type of policy to create. You can specify one of the following values: AISERVICES_OPT_OUT_POLICY, BACKUP_POLICY, SERVICE_CONTROL_POLICY, TAG_POLICY
func (o PolicyOutput) Type() PolicyTypeOutput {
	return o.ApplyT(func(v *Policy) PolicyTypeOutput { return v.Type }).(PolicyTypeOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*PolicyInput)(nil)).Elem(), &Policy{})
	pulumi.RegisterOutputType(PolicyOutput{})
}
