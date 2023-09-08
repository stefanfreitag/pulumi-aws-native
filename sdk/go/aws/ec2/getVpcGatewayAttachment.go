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

// Resource Type definition for AWS::EC2::VPCGatewayAttachment
func LookupVpcGatewayAttachment(ctx *pulumi.Context, args *LookupVpcGatewayAttachmentArgs, opts ...pulumi.InvokeOption) (*LookupVpcGatewayAttachmentResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVpcGatewayAttachmentResult
	err := ctx.Invoke("aws-native:ec2:getVpcGatewayAttachment", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupVpcGatewayAttachmentArgs struct {
	Id string `pulumi:"id"`
}

type LookupVpcGatewayAttachmentResult struct {
	Id                *string `pulumi:"id"`
	InternetGatewayId *string `pulumi:"internetGatewayId"`
	VpcId             *string `pulumi:"vpcId"`
	VpnGatewayId      *string `pulumi:"vpnGatewayId"`
}

func LookupVpcGatewayAttachmentOutput(ctx *pulumi.Context, args LookupVpcGatewayAttachmentOutputArgs, opts ...pulumi.InvokeOption) LookupVpcGatewayAttachmentResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupVpcGatewayAttachmentResult, error) {
			args := v.(LookupVpcGatewayAttachmentArgs)
			r, err := LookupVpcGatewayAttachment(ctx, &args, opts...)
			var s LookupVpcGatewayAttachmentResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupVpcGatewayAttachmentResultOutput)
}

type LookupVpcGatewayAttachmentOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupVpcGatewayAttachmentOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpcGatewayAttachmentArgs)(nil)).Elem()
}

type LookupVpcGatewayAttachmentResultOutput struct{ *pulumi.OutputState }

func (LookupVpcGatewayAttachmentResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupVpcGatewayAttachmentResult)(nil)).Elem()
}

func (o LookupVpcGatewayAttachmentResultOutput) ToLookupVpcGatewayAttachmentResultOutput() LookupVpcGatewayAttachmentResultOutput {
	return o
}

func (o LookupVpcGatewayAttachmentResultOutput) ToLookupVpcGatewayAttachmentResultOutputWithContext(ctx context.Context) LookupVpcGatewayAttachmentResultOutput {
	return o
}

func (o LookupVpcGatewayAttachmentResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupVpcGatewayAttachmentResult] {
	return pulumix.Output[LookupVpcGatewayAttachmentResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupVpcGatewayAttachmentResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcGatewayAttachmentResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupVpcGatewayAttachmentResultOutput) InternetGatewayId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcGatewayAttachmentResult) *string { return v.InternetGatewayId }).(pulumi.StringPtrOutput)
}

func (o LookupVpcGatewayAttachmentResultOutput) VpcId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcGatewayAttachmentResult) *string { return v.VpcId }).(pulumi.StringPtrOutput)
}

func (o LookupVpcGatewayAttachmentResultOutput) VpnGatewayId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupVpcGatewayAttachmentResult) *string { return v.VpnGatewayId }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupVpcGatewayAttachmentResultOutput{})
}
