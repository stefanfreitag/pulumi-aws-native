// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package groundstation

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS Ground Station Mission Profile resource type for CloudFormation.
func LookupMissionProfile(ctx *pulumi.Context, args *LookupMissionProfileArgs, opts ...pulumi.InvokeOption) (*LookupMissionProfileResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupMissionProfileResult
	err := ctx.Invoke("aws-native:groundstation:getMissionProfile", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupMissionProfileArgs struct {
	Arn string `pulumi:"arn"`
	Id  string `pulumi:"id"`
}

type LookupMissionProfileResult struct {
	Arn *string `pulumi:"arn"`
	// Post-pass time needed after the contact.
	ContactPostPassDurationSeconds *int `pulumi:"contactPostPassDurationSeconds"`
	// Pre-pass time needed before the contact.
	ContactPrePassDurationSeconds *int                         `pulumi:"contactPrePassDurationSeconds"`
	DataflowEdges                 []MissionProfileDataflowEdge `pulumi:"dataflowEdges"`
	Id                            *string                      `pulumi:"id"`
	// Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
	MinimumViableContactDurationSeconds *int `pulumi:"minimumViableContactDurationSeconds"`
	// A name used to identify a mission profile.
	Name   *string `pulumi:"name"`
	Region *string `pulumi:"region"`
	// The ARN of a KMS Key used for encrypting data during transmission from the source to destination locations.
	StreamsKmsKey *MissionProfileStreamsKmsKey `pulumi:"streamsKmsKey"`
	// The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.
	StreamsKmsRole    *string   `pulumi:"streamsKmsRole"`
	Tags              []aws.Tag `pulumi:"tags"`
	TrackingConfigArn *string   `pulumi:"trackingConfigArn"`
}

func LookupMissionProfileOutput(ctx *pulumi.Context, args LookupMissionProfileOutputArgs, opts ...pulumi.InvokeOption) LookupMissionProfileResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupMissionProfileResult, error) {
			args := v.(LookupMissionProfileArgs)
			r, err := LookupMissionProfile(ctx, &args, opts...)
			var s LookupMissionProfileResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupMissionProfileResultOutput)
}

type LookupMissionProfileOutputArgs struct {
	Arn pulumi.StringInput `pulumi:"arn"`
	Id  pulumi.StringInput `pulumi:"id"`
}

func (LookupMissionProfileOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMissionProfileArgs)(nil)).Elem()
}

type LookupMissionProfileResultOutput struct{ *pulumi.OutputState }

func (LookupMissionProfileResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupMissionProfileResult)(nil)).Elem()
}

func (o LookupMissionProfileResultOutput) ToLookupMissionProfileResultOutput() LookupMissionProfileResultOutput {
	return o
}

func (o LookupMissionProfileResultOutput) ToLookupMissionProfileResultOutputWithContext(ctx context.Context) LookupMissionProfileResultOutput {
	return o
}

func (o LookupMissionProfileResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Post-pass time needed after the contact.
func (o LookupMissionProfileResultOutput) ContactPostPassDurationSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *int { return v.ContactPostPassDurationSeconds }).(pulumi.IntPtrOutput)
}

// Pre-pass time needed before the contact.
func (o LookupMissionProfileResultOutput) ContactPrePassDurationSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *int { return v.ContactPrePassDurationSeconds }).(pulumi.IntPtrOutput)
}

func (o LookupMissionProfileResultOutput) DataflowEdges() MissionProfileDataflowEdgeArrayOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) []MissionProfileDataflowEdge { return v.DataflowEdges }).(MissionProfileDataflowEdgeArrayOutput)
}

func (o LookupMissionProfileResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// Visibilities with shorter duration than the specified minimum viable contact duration will be ignored when searching for available contacts.
func (o LookupMissionProfileResultOutput) MinimumViableContactDurationSeconds() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *int { return v.MinimumViableContactDurationSeconds }).(pulumi.IntPtrOutput)
}

// A name used to identify a mission profile.
func (o LookupMissionProfileResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupMissionProfileResultOutput) Region() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *string { return v.Region }).(pulumi.StringPtrOutput)
}

// The ARN of a KMS Key used for encrypting data during transmission from the source to destination locations.
func (o LookupMissionProfileResultOutput) StreamsKmsKey() MissionProfileStreamsKmsKeyPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *MissionProfileStreamsKmsKey { return v.StreamsKmsKey }).(MissionProfileStreamsKmsKeyPtrOutput)
}

// The ARN of the KMS Key or Alias Key role used to define permissions on KMS Key usage.
func (o LookupMissionProfileResultOutput) StreamsKmsRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *string { return v.StreamsKmsRole }).(pulumi.StringPtrOutput)
}

func (o LookupMissionProfileResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func (o LookupMissionProfileResultOutput) TrackingConfigArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupMissionProfileResult) *string { return v.TrackingConfigArn }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupMissionProfileResultOutput{})
}
