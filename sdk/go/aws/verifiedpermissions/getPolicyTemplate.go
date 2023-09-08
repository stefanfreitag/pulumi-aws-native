// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package verifiedpermissions

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Definition of AWS::VerifiedPermissions::PolicyTemplate Resource Type
func LookupPolicyTemplate(ctx *pulumi.Context, args *LookupPolicyTemplateArgs, opts ...pulumi.InvokeOption) (*LookupPolicyTemplateResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupPolicyTemplateResult
	err := ctx.Invoke("aws-native:verifiedpermissions:getPolicyTemplate", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupPolicyTemplateArgs struct {
	PolicyStoreId    string `pulumi:"policyStoreId"`
	PolicyTemplateId string `pulumi:"policyTemplateId"`
}

type LookupPolicyTemplateResult struct {
	Description      *string `pulumi:"description"`
	PolicyTemplateId *string `pulumi:"policyTemplateId"`
	Statement        *string `pulumi:"statement"`
}

func LookupPolicyTemplateOutput(ctx *pulumi.Context, args LookupPolicyTemplateOutputArgs, opts ...pulumi.InvokeOption) LookupPolicyTemplateResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupPolicyTemplateResult, error) {
			args := v.(LookupPolicyTemplateArgs)
			r, err := LookupPolicyTemplate(ctx, &args, opts...)
			var s LookupPolicyTemplateResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupPolicyTemplateResultOutput)
}

type LookupPolicyTemplateOutputArgs struct {
	PolicyStoreId    pulumi.StringInput `pulumi:"policyStoreId"`
	PolicyTemplateId pulumi.StringInput `pulumi:"policyTemplateId"`
}

func (LookupPolicyTemplateOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPolicyTemplateArgs)(nil)).Elem()
}

type LookupPolicyTemplateResultOutput struct{ *pulumi.OutputState }

func (LookupPolicyTemplateResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupPolicyTemplateResult)(nil)).Elem()
}

func (o LookupPolicyTemplateResultOutput) ToLookupPolicyTemplateResultOutput() LookupPolicyTemplateResultOutput {
	return o
}

func (o LookupPolicyTemplateResultOutput) ToLookupPolicyTemplateResultOutputWithContext(ctx context.Context) LookupPolicyTemplateResultOutput {
	return o
}

func (o LookupPolicyTemplateResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupPolicyTemplateResult] {
	return pulumix.Output[LookupPolicyTemplateResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupPolicyTemplateResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPolicyTemplateResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o LookupPolicyTemplateResultOutput) PolicyTemplateId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPolicyTemplateResult) *string { return v.PolicyTemplateId }).(pulumi.StringPtrOutput)
}

func (o LookupPolicyTemplateResultOutput) Statement() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupPolicyTemplateResult) *string { return v.Statement }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupPolicyTemplateResultOutput{})
}
