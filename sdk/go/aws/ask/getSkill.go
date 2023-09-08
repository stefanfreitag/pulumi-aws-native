// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ask

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for Alexa::ASK::Skill
func LookupSkill(ctx *pulumi.Context, args *LookupSkillArgs, opts ...pulumi.InvokeOption) (*LookupSkillResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSkillResult
	err := ctx.Invoke("aws-native:ask:getSkill", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSkillArgs struct {
	Id string `pulumi:"id"`
}

type LookupSkillResult struct {
	AuthenticationConfiguration *SkillAuthenticationConfiguration `pulumi:"authenticationConfiguration"`
	Id                          *string                           `pulumi:"id"`
	SkillPackage                *SkillPackage                     `pulumi:"skillPackage"`
}

func LookupSkillOutput(ctx *pulumi.Context, args LookupSkillOutputArgs, opts ...pulumi.InvokeOption) LookupSkillResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSkillResult, error) {
			args := v.(LookupSkillArgs)
			r, err := LookupSkill(ctx, &args, opts...)
			var s LookupSkillResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSkillResultOutput)
}

type LookupSkillOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupSkillOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSkillArgs)(nil)).Elem()
}

type LookupSkillResultOutput struct{ *pulumi.OutputState }

func (LookupSkillResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSkillResult)(nil)).Elem()
}

func (o LookupSkillResultOutput) ToLookupSkillResultOutput() LookupSkillResultOutput {
	return o
}

func (o LookupSkillResultOutput) ToLookupSkillResultOutputWithContext(ctx context.Context) LookupSkillResultOutput {
	return o
}

func (o LookupSkillResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSkillResult] {
	return pulumix.Output[LookupSkillResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupSkillResultOutput) AuthenticationConfiguration() SkillAuthenticationConfigurationPtrOutput {
	return o.ApplyT(func(v LookupSkillResult) *SkillAuthenticationConfiguration { return v.AuthenticationConfiguration }).(SkillAuthenticationConfigurationPtrOutput)
}

func (o LookupSkillResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSkillResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupSkillResultOutput) SkillPackage() SkillPackagePtrOutput {
	return o.ApplyT(func(v LookupSkillResult) *SkillPackage { return v.SkillPackage }).(SkillPackagePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSkillResultOutput{})
}
