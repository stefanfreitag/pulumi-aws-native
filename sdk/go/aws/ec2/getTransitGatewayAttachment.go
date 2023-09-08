// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::TransitGatewayAttachment
func LookupTransitGatewayAttachment(ctx *pulumi.Context, args *LookupTransitGatewayAttachmentArgs, opts ...pulumi.InvokeOption) (*LookupTransitGatewayAttachmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupTransitGatewayAttachmentResult
	err := ctx.Invoke("aws-native:ec2:getTransitGatewayAttachment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupTransitGatewayAttachmentArgs struct {
	Id string `pulumi:"id"`
}

type LookupTransitGatewayAttachmentResult struct {
	Id *string `pulumi:"id"`
	// The options for the transit gateway vpc attachment.
	Options   *OptionsProperties            `pulumi:"options"`
	SubnetIds []string                      `pulumi:"subnetIds"`
	Tags      []TransitGatewayAttachmentTag `pulumi:"tags"`
}

func LookupTransitGatewayAttachmentOutput(ctx *pulumi.Context, args LookupTransitGatewayAttachmentOutputArgs, opts ...pulumi.InvokeOption) LookupTransitGatewayAttachmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupTransitGatewayAttachmentResult, error) {
			args := v.(LookupTransitGatewayAttachmentArgs)
			r, err := LookupTransitGatewayAttachment(ctx, &args, opts...)
			var s LookupTransitGatewayAttachmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupTransitGatewayAttachmentResultOutput)
}

type LookupTransitGatewayAttachmentOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupTransitGatewayAttachmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayAttachmentArgs)(nil)).Elem()
}

type LookupTransitGatewayAttachmentResultOutput struct{ *pulumi.OutputState }

func (LookupTransitGatewayAttachmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupTransitGatewayAttachmentResult)(nil)).Elem()
}

func (o LookupTransitGatewayAttachmentResultOutput) ToLookupTransitGatewayAttachmentResultOutput() LookupTransitGatewayAttachmentResultOutput {
	return o
}

func (o LookupTransitGatewayAttachmentResultOutput) ToLookupTransitGatewayAttachmentResultOutputWithContext(ctx context.Context) LookupTransitGatewayAttachmentResultOutput {
	return o
}

func (o LookupTransitGatewayAttachmentResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupTransitGatewayAttachmentResult] {
	return pulumix.Output[LookupTransitGatewayAttachmentResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupTransitGatewayAttachmentResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayAttachmentResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// The options for the transit gateway vpc attachment.
func (o LookupTransitGatewayAttachmentResultOutput) Options() OptionsPropertiesPtrOutput {
	return o.ApplyT(func(v LookupTransitGatewayAttachmentResult) *OptionsProperties { return v.Options }).(OptionsPropertiesPtrOutput)
}

func (o LookupTransitGatewayAttachmentResultOutput) SubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupTransitGatewayAttachmentResult) []string { return v.SubnetIds }).(pulumi.StringArrayOutput)
}

func (o LookupTransitGatewayAttachmentResultOutput) Tags() TransitGatewayAttachmentTagArrayOutput {
	return o.ApplyT(func(v LookupTransitGatewayAttachmentResult) []TransitGatewayAttachmentTag { return v.Tags }).(TransitGatewayAttachmentTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupTransitGatewayAttachmentResultOutput{})
}
