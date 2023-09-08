// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ses

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::SES::EmailIdentity
func LookupEmailIdentity(ctx *pulumi.Context, args *LookupEmailIdentityArgs, opts ...pulumi.InvokeOption) (*LookupEmailIdentityResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupEmailIdentityResult
	err := ctx.Invoke("aws-native:ses:getEmailIdentity", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupEmailIdentityArgs struct {
	// The email address or domain to verify.
	EmailIdentity string `pulumi:"emailIdentity"`
}

type LookupEmailIdentityResult struct {
	ConfigurationSetAttributes *EmailIdentityConfigurationSetAttributes `pulumi:"configurationSetAttributes"`
	DkimAttributes             *EmailIdentityDkimAttributes             `pulumi:"dkimAttributes"`
	DkimDnsTokenName1          *string                                  `pulumi:"dkimDnsTokenName1"`
	DkimDnsTokenName2          *string                                  `pulumi:"dkimDnsTokenName2"`
	DkimDnsTokenName3          *string                                  `pulumi:"dkimDnsTokenName3"`
	DkimDnsTokenValue1         *string                                  `pulumi:"dkimDnsTokenValue1"`
	DkimDnsTokenValue2         *string                                  `pulumi:"dkimDnsTokenValue2"`
	DkimDnsTokenValue3         *string                                  `pulumi:"dkimDnsTokenValue3"`
	DkimSigningAttributes      *EmailIdentityDkimSigningAttributes      `pulumi:"dkimSigningAttributes"`
	FeedbackAttributes         *EmailIdentityFeedbackAttributes         `pulumi:"feedbackAttributes"`
	MailFromAttributes         *EmailIdentityMailFromAttributes         `pulumi:"mailFromAttributes"`
}

func LookupEmailIdentityOutput(ctx *pulumi.Context, args LookupEmailIdentityOutputArgs, opts ...pulumi.InvokeOption) LookupEmailIdentityResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupEmailIdentityResult, error) {
			args := v.(LookupEmailIdentityArgs)
			r, err := LookupEmailIdentity(ctx, &args, opts...)
			var s LookupEmailIdentityResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupEmailIdentityResultOutput)
}

type LookupEmailIdentityOutputArgs struct {
	// The email address or domain to verify.
	EmailIdentity pulumi.StringInput `pulumi:"emailIdentity"`
}

func (LookupEmailIdentityOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEmailIdentityArgs)(nil)).Elem()
}

type LookupEmailIdentityResultOutput struct{ *pulumi.OutputState }

func (LookupEmailIdentityResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupEmailIdentityResult)(nil)).Elem()
}

func (o LookupEmailIdentityResultOutput) ToLookupEmailIdentityResultOutput() LookupEmailIdentityResultOutput {
	return o
}

func (o LookupEmailIdentityResultOutput) ToLookupEmailIdentityResultOutputWithContext(ctx context.Context) LookupEmailIdentityResultOutput {
	return o
}

func (o LookupEmailIdentityResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupEmailIdentityResult] {
	return pulumix.Output[LookupEmailIdentityResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupEmailIdentityResultOutput) ConfigurationSetAttributes() EmailIdentityConfigurationSetAttributesPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *EmailIdentityConfigurationSetAttributes {
		return v.ConfigurationSetAttributes
	}).(EmailIdentityConfigurationSetAttributesPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimAttributes() EmailIdentityDkimAttributesPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *EmailIdentityDkimAttributes { return v.DkimAttributes }).(EmailIdentityDkimAttributesPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimDnsTokenName1() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *string { return v.DkimDnsTokenName1 }).(pulumi.StringPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimDnsTokenName2() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *string { return v.DkimDnsTokenName2 }).(pulumi.StringPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimDnsTokenName3() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *string { return v.DkimDnsTokenName3 }).(pulumi.StringPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimDnsTokenValue1() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *string { return v.DkimDnsTokenValue1 }).(pulumi.StringPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimDnsTokenValue2() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *string { return v.DkimDnsTokenValue2 }).(pulumi.StringPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimDnsTokenValue3() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *string { return v.DkimDnsTokenValue3 }).(pulumi.StringPtrOutput)
}

func (o LookupEmailIdentityResultOutput) DkimSigningAttributes() EmailIdentityDkimSigningAttributesPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *EmailIdentityDkimSigningAttributes { return v.DkimSigningAttributes }).(EmailIdentityDkimSigningAttributesPtrOutput)
}

func (o LookupEmailIdentityResultOutput) FeedbackAttributes() EmailIdentityFeedbackAttributesPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *EmailIdentityFeedbackAttributes { return v.FeedbackAttributes }).(EmailIdentityFeedbackAttributesPtrOutput)
}

func (o LookupEmailIdentityResultOutput) MailFromAttributes() EmailIdentityMailFromAttributesPtrOutput {
	return o.ApplyT(func(v LookupEmailIdentityResult) *EmailIdentityMailFromAttributes { return v.MailFromAttributes }).(EmailIdentityMailFromAttributesPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupEmailIdentityResultOutput{})
}
