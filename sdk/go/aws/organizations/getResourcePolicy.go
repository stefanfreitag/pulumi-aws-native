// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package organizations

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// You can use AWS::Organizations::ResourcePolicy to delegate policy management for AWS Organizations to specified member accounts to perform policy actions that are by default available only to the management account.
func LookupResourcePolicy(ctx *pulumi.Context, args *LookupResourcePolicyArgs, opts ...pulumi.InvokeOption) (*LookupResourcePolicyResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResourcePolicyResult
	err := ctx.Invoke("aws-native:organizations:getResourcePolicy", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResourcePolicyArgs struct {
	// The unique identifier (ID) associated with this resource policy.
	Id string `pulumi:"id"`
}

type LookupResourcePolicyResult struct {
	// The Amazon Resource Name (ARN) of the resource policy.
	Arn *string `pulumi:"arn"`
	// The policy document. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Organizations::ResourcePolicy` for more information about the expected schema for this property.
	Content interface{} `pulumi:"content"`
	// The unique identifier (ID) associated with this resource policy.
	Id *string `pulumi:"id"`
	// A list of tags that you want to attach to the resource policy
	Tags []ResourcePolicyTag `pulumi:"tags"`
}

func LookupResourcePolicyOutput(ctx *pulumi.Context, args LookupResourcePolicyOutputArgs, opts ...pulumi.InvokeOption) LookupResourcePolicyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResourcePolicyResult, error) {
			args := v.(LookupResourcePolicyArgs)
			r, err := LookupResourcePolicy(ctx, &args, opts...)
			var s LookupResourcePolicyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResourcePolicyResultOutput)
}

type LookupResourcePolicyOutputArgs struct {
	// The unique identifier (ID) associated with this resource policy.
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupResourcePolicyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourcePolicyArgs)(nil)).Elem()
}

type LookupResourcePolicyResultOutput struct{ *pulumi.OutputState }

func (LookupResourcePolicyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResourcePolicyResult)(nil)).Elem()
}

func (o LookupResourcePolicyResultOutput) ToLookupResourcePolicyResultOutput() LookupResourcePolicyResultOutput {
	return o
}

func (o LookupResourcePolicyResultOutput) ToLookupResourcePolicyResultOutputWithContext(ctx context.Context) LookupResourcePolicyResultOutput {
	return o
}

// The Amazon Resource Name (ARN) of the resource policy.
func (o LookupResourcePolicyResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// The policy document. For AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation always converts a YAML policy to JSON format before submitting it.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Organizations::ResourcePolicy` for more information about the expected schema for this property.
func (o LookupResourcePolicyResultOutput) Content() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) interface{} { return v.Content }).(pulumi.AnyOutput)
}

// The unique identifier (ID) associated with this resource policy.
func (o LookupResourcePolicyResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// A list of tags that you want to attach to the resource policy
func (o LookupResourcePolicyResultOutput) Tags() ResourcePolicyTagArrayOutput {
	return o.ApplyT(func(v LookupResourcePolicyResult) []ResourcePolicyTag { return v.Tags }).(ResourcePolicyTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResourcePolicyResultOutput{})
}
