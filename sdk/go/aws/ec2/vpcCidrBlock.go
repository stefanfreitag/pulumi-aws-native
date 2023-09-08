// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::EC2::VPCCidrBlock
//
// Deprecated: VpcCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type VpcCidrBlock struct {
	pulumi.CustomResourceState

	AmazonProvidedIpv6CidrBlock pulumi.BoolPtrOutput   `pulumi:"amazonProvidedIpv6CidrBlock"`
	CidrBlock                   pulumi.StringPtrOutput `pulumi:"cidrBlock"`
	Ipv4IpamPoolId              pulumi.StringPtrOutput `pulumi:"ipv4IpamPoolId"`
	Ipv4NetmaskLength           pulumi.IntPtrOutput    `pulumi:"ipv4NetmaskLength"`
	Ipv6CidrBlock               pulumi.StringPtrOutput `pulumi:"ipv6CidrBlock"`
	Ipv6IpamPoolId              pulumi.StringPtrOutput `pulumi:"ipv6IpamPoolId"`
	Ipv6NetmaskLength           pulumi.IntPtrOutput    `pulumi:"ipv6NetmaskLength"`
	Ipv6Pool                    pulumi.StringPtrOutput `pulumi:"ipv6Pool"`
	VpcId                       pulumi.StringOutput    `pulumi:"vpcId"`
}

// NewVpcCidrBlock registers a new resource with the given unique name, arguments, and options.
func NewVpcCidrBlock(ctx *pulumi.Context,
	name string, args *VpcCidrBlockArgs, opts ...pulumi.ResourceOption) (*VpcCidrBlock, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.VpcId == nil {
		return nil, errors.New("invalid value for required argument 'VpcId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"amazonProvidedIpv6CidrBlock",
		"cidrBlock",
		"ipv4IpamPoolId",
		"ipv4NetmaskLength",
		"ipv6CidrBlock",
		"ipv6IpamPoolId",
		"ipv6NetmaskLength",
		"ipv6Pool",
		"vpcId",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource VpcCidrBlock
	err := ctx.RegisterResource("aws-native:ec2:VpcCidrBlock", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVpcCidrBlock gets an existing VpcCidrBlock resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVpcCidrBlock(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VpcCidrBlockState, opts ...pulumi.ResourceOption) (*VpcCidrBlock, error) {
	var resource VpcCidrBlock
	err := ctx.ReadResource("aws-native:ec2:VpcCidrBlock", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VpcCidrBlock resources.
type vpcCidrBlockState struct {
}

type VpcCidrBlockState struct {
}

func (VpcCidrBlockState) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcCidrBlockState)(nil)).Elem()
}

type vpcCidrBlockArgs struct {
	AmazonProvidedIpv6CidrBlock *bool   `pulumi:"amazonProvidedIpv6CidrBlock"`
	CidrBlock                   *string `pulumi:"cidrBlock"`
	Ipv4IpamPoolId              *string `pulumi:"ipv4IpamPoolId"`
	Ipv4NetmaskLength           *int    `pulumi:"ipv4NetmaskLength"`
	Ipv6CidrBlock               *string `pulumi:"ipv6CidrBlock"`
	Ipv6IpamPoolId              *string `pulumi:"ipv6IpamPoolId"`
	Ipv6NetmaskLength           *int    `pulumi:"ipv6NetmaskLength"`
	Ipv6Pool                    *string `pulumi:"ipv6Pool"`
	VpcId                       string  `pulumi:"vpcId"`
}

// The set of arguments for constructing a VpcCidrBlock resource.
type VpcCidrBlockArgs struct {
	AmazonProvidedIpv6CidrBlock pulumi.BoolPtrInput
	CidrBlock                   pulumi.StringPtrInput
	Ipv4IpamPoolId              pulumi.StringPtrInput
	Ipv4NetmaskLength           pulumi.IntPtrInput
	Ipv6CidrBlock               pulumi.StringPtrInput
	Ipv6IpamPoolId              pulumi.StringPtrInput
	Ipv6NetmaskLength           pulumi.IntPtrInput
	Ipv6Pool                    pulumi.StringPtrInput
	VpcId                       pulumi.StringInput
}

func (VpcCidrBlockArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vpcCidrBlockArgs)(nil)).Elem()
}

type VpcCidrBlockInput interface {
	pulumi.Input

	ToVpcCidrBlockOutput() VpcCidrBlockOutput
	ToVpcCidrBlockOutputWithContext(ctx context.Context) VpcCidrBlockOutput
}

func (*VpcCidrBlock) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcCidrBlock)(nil)).Elem()
}

func (i *VpcCidrBlock) ToVpcCidrBlockOutput() VpcCidrBlockOutput {
	return i.ToVpcCidrBlockOutputWithContext(context.Background())
}

func (i *VpcCidrBlock) ToVpcCidrBlockOutputWithContext(ctx context.Context) VpcCidrBlockOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VpcCidrBlockOutput)
}

func (i *VpcCidrBlock) ToOutput(ctx context.Context) pulumix.Output[*VpcCidrBlock] {
	return pulumix.Output[*VpcCidrBlock]{
		OutputState: i.ToVpcCidrBlockOutputWithContext(ctx).OutputState,
	}
}

type VpcCidrBlockOutput struct{ *pulumi.OutputState }

func (VpcCidrBlockOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VpcCidrBlock)(nil)).Elem()
}

func (o VpcCidrBlockOutput) ToVpcCidrBlockOutput() VpcCidrBlockOutput {
	return o
}

func (o VpcCidrBlockOutput) ToVpcCidrBlockOutputWithContext(ctx context.Context) VpcCidrBlockOutput {
	return o
}

func (o VpcCidrBlockOutput) ToOutput(ctx context.Context) pulumix.Output[*VpcCidrBlock] {
	return pulumix.Output[*VpcCidrBlock]{
		OutputState: o.OutputState,
	}
}

func (o VpcCidrBlockOutput) AmazonProvidedIpv6CidrBlock() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.BoolPtrOutput { return v.AmazonProvidedIpv6CidrBlock }).(pulumi.BoolPtrOutput)
}

func (o VpcCidrBlockOutput) CidrBlock() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.StringPtrOutput { return v.CidrBlock }).(pulumi.StringPtrOutput)
}

func (o VpcCidrBlockOutput) Ipv4IpamPoolId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.StringPtrOutput { return v.Ipv4IpamPoolId }).(pulumi.StringPtrOutput)
}

func (o VpcCidrBlockOutput) Ipv4NetmaskLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.IntPtrOutput { return v.Ipv4NetmaskLength }).(pulumi.IntPtrOutput)
}

func (o VpcCidrBlockOutput) Ipv6CidrBlock() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.StringPtrOutput { return v.Ipv6CidrBlock }).(pulumi.StringPtrOutput)
}

func (o VpcCidrBlockOutput) Ipv6IpamPoolId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.StringPtrOutput { return v.Ipv6IpamPoolId }).(pulumi.StringPtrOutput)
}

func (o VpcCidrBlockOutput) Ipv6NetmaskLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.IntPtrOutput { return v.Ipv6NetmaskLength }).(pulumi.IntPtrOutput)
}

func (o VpcCidrBlockOutput) Ipv6Pool() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.StringPtrOutput { return v.Ipv6Pool }).(pulumi.StringPtrOutput)
}

func (o VpcCidrBlockOutput) VpcId() pulumi.StringOutput {
	return o.ApplyT(func(v *VpcCidrBlock) pulumi.StringOutput { return v.VpcId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*VpcCidrBlockInput)(nil)).Elem(), &VpcCidrBlock{})
	pulumi.RegisterOutputType(VpcCidrBlockOutput{})
}
