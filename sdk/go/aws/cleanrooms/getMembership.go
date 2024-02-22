// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package cleanrooms

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Represents an AWS account that is a part of a collaboration
func LookupMembership(ctx *pulumi.Context, args *LookupMembershipArgs, opts ...pulumi.InvokeOption) (*LookupMembershipResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMembershipResult
	err := ctx.Invoke("aws-native:cleanrooms:getMembership", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMembershipArgs struct {
	MembershipIdentifier string `pulumi:"membershipIdentifier"`
}

type LookupMembershipResult struct {
	Arn                           *string                                      `pulumi:"arn"`
	CollaborationArn              *string                                      `pulumi:"collaborationArn"`
	CollaborationCreatorAccountId *string                                      `pulumi:"collaborationCreatorAccountId"`
	DefaultResultConfiguration    *MembershipProtectedQueryResultConfiguration `pulumi:"defaultResultConfiguration"`
	MembershipIdentifier          *string                                      `pulumi:"membershipIdentifier"`
	PaymentConfiguration          *MembershipPaymentConfiguration              `pulumi:"paymentConfiguration"`
	QueryLogStatus                *MembershipQueryLogStatus                    `pulumi:"queryLogStatus"`
	// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupMembershipOutput(ctx *pulumi.Context, args LookupMembershipOutputArgs, opts ...pulumi.InvokeOption) LookupMembershipResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMembershipResult, error) {
			args := v.(LookupMembershipArgs)
			r, err := LookupMembership(ctx, &args, opts...)
			var s LookupMembershipResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMembershipResultOutput)
}

type LookupMembershipOutputArgs struct {
	MembershipIdentifier pulumi.StringInput `pulumi:"membershipIdentifier"`
}

func (LookupMembershipOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMembershipArgs)(nil)).Elem()
}

type LookupMembershipResultOutput struct{ *pulumi.OutputState }

func (LookupMembershipResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMembershipResult)(nil)).Elem()
}

func (o LookupMembershipResultOutput) ToLookupMembershipResultOutput() LookupMembershipResultOutput {
	return o
}

func (o LookupMembershipResultOutput) ToLookupMembershipResultOutputWithContext(ctx context.Context) LookupMembershipResultOutput {
	return o
}

func (o LookupMembershipResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMembershipResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupMembershipResultOutput) CollaborationArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMembershipResult) *string { return v.CollaborationArn }).(pulumi.StringPtrOutput)
}

func (o LookupMembershipResultOutput) CollaborationCreatorAccountId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMembershipResult) *string { return v.CollaborationCreatorAccountId }).(pulumi.StringPtrOutput)
}

func (o LookupMembershipResultOutput) DefaultResultConfiguration() MembershipProtectedQueryResultConfigurationPtrOutput {
	return o.ApplyT(func(v LookupMembershipResult) *MembershipProtectedQueryResultConfiguration {
		return v.DefaultResultConfiguration
	}).(MembershipProtectedQueryResultConfigurationPtrOutput)
}

func (o LookupMembershipResultOutput) MembershipIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMembershipResult) *string { return v.MembershipIdentifier }).(pulumi.StringPtrOutput)
}

func (o LookupMembershipResultOutput) PaymentConfiguration() MembershipPaymentConfigurationPtrOutput {
	return o.ApplyT(func(v LookupMembershipResult) *MembershipPaymentConfiguration { return v.PaymentConfiguration }).(MembershipPaymentConfigurationPtrOutput)
}

func (o LookupMembershipResultOutput) QueryLogStatus() MembershipQueryLogStatusPtrOutput {
	return o.ApplyT(func(v LookupMembershipResult) *MembershipQueryLogStatus { return v.QueryLogStatus }).(MembershipQueryLogStatusPtrOutput)
}

// An arbitrary set of tags (key-value pairs) for this cleanrooms membership.
func (o LookupMembershipResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupMembershipResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMembershipResultOutput{})
}
