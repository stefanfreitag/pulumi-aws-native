// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package signer

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A signing profile is a signing template that can be used to carry out a pre-defined signing job.
func LookupSigningProfile(ctx *pulumi.Context, args *LookupSigningProfileArgs, opts ...pulumi.InvokeOption) (*LookupSigningProfileResult, error) {
	var rv LookupSigningProfileResult
	err := ctx.Invoke("aws-native:signer:getSigningProfile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSigningProfileArgs struct {
	// The Amazon Resource Name (ARN) of the specified signing profile.
	Arn string `pulumi:"arn"`
}

type LookupSigningProfileResult struct {
	// The Amazon Resource Name (ARN) of the specified signing profile.
	Arn *string `pulumi:"arn"`
	// A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name.
	ProfileName *string `pulumi:"profileName"`
	// A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.
	ProfileVersion *string `pulumi:"profileVersion"`
	// The Amazon Resource Name (ARN) of the specified signing profile version.
	ProfileVersionArn *string `pulumi:"profileVersionArn"`
	// A list of tags associated with the signing profile.
	Tags []SigningProfileTag `pulumi:"tags"`
}

func LookupSigningProfileOutput(ctx *pulumi.Context, args LookupSigningProfileOutputArgs, opts ...pulumi.InvokeOption) LookupSigningProfileResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSigningProfileResult, error) {
			args := v.(LookupSigningProfileArgs)
			r, err := LookupSigningProfile(ctx, &args, opts...)
			var s LookupSigningProfileResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSigningProfileResultOutput)
}

type LookupSigningProfileOutputArgs struct {
	// The Amazon Resource Name (ARN) of the specified signing profile.
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupSigningProfileOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSigningProfileArgs)(nil)).Elem()
}

type LookupSigningProfileResultOutput struct{ *pulumi.OutputState }

func (LookupSigningProfileResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSigningProfileResult)(nil)).Elem()
}

func (o LookupSigningProfileResultOutput) ToLookupSigningProfileResultOutput() LookupSigningProfileResultOutput {
	return o
}

func (o LookupSigningProfileResultOutput) ToLookupSigningProfileResultOutputWithContext(ctx context.Context) LookupSigningProfileResultOutput {
	return o
}

// The Amazon Resource Name (ARN) of the specified signing profile.
func (o LookupSigningProfileResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSigningProfileResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name.
func (o LookupSigningProfileResultOutput) ProfileName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSigningProfileResult) *string { return v.ProfileName }).(pulumi.StringPtrOutput)
}

// A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.
func (o LookupSigningProfileResultOutput) ProfileVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSigningProfileResult) *string { return v.ProfileVersion }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the specified signing profile version.
func (o LookupSigningProfileResultOutput) ProfileVersionArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSigningProfileResult) *string { return v.ProfileVersionArn }).(pulumi.StringPtrOutput)
}

// A list of tags associated with the signing profile.
func (o LookupSigningProfileResultOutput) Tags() SigningProfileTagArrayOutput {
	return o.ApplyT(func(v LookupSigningProfileResult) []SigningProfileTag { return v.Tags }).(SigningProfileTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSigningProfileResultOutput{})
}
