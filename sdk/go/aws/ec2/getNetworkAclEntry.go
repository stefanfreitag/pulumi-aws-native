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

// Resource Type definition for AWS::EC2::NetworkAclEntry
func LookupNetworkAclEntry(ctx *pulumi.Context, args *LookupNetworkAclEntryArgs, opts ...pulumi.InvokeOption) (*LookupNetworkAclEntryResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupNetworkAclEntryResult
	err := ctx.Invoke("aws-native:ec2:getNetworkAclEntry", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupNetworkAclEntryArgs struct {
	Id string `pulumi:"id"`
}

type LookupNetworkAclEntryResult struct {
	CidrBlock     *string                   `pulumi:"cidrBlock"`
	Icmp          *NetworkAclEntryIcmp      `pulumi:"icmp"`
	Id            *string                   `pulumi:"id"`
	Ipv6CidrBlock *string                   `pulumi:"ipv6CidrBlock"`
	PortRange     *NetworkAclEntryPortRange `pulumi:"portRange"`
	Protocol      *int                      `pulumi:"protocol"`
	RuleAction    *string                   `pulumi:"ruleAction"`
}

func LookupNetworkAclEntryOutput(ctx *pulumi.Context, args LookupNetworkAclEntryOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkAclEntryResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNetworkAclEntryResult, error) {
			args := v.(LookupNetworkAclEntryArgs)
			r, err := LookupNetworkAclEntry(ctx, &args, opts...)
			var s LookupNetworkAclEntryResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNetworkAclEntryResultOutput)
}

type LookupNetworkAclEntryOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupNetworkAclEntryOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkAclEntryArgs)(nil)).Elem()
}

type LookupNetworkAclEntryResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkAclEntryResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkAclEntryResult)(nil)).Elem()
}

func (o LookupNetworkAclEntryResultOutput) ToLookupNetworkAclEntryResultOutput() LookupNetworkAclEntryResultOutput {
	return o
}

func (o LookupNetworkAclEntryResultOutput) ToLookupNetworkAclEntryResultOutputWithContext(ctx context.Context) LookupNetworkAclEntryResultOutput {
	return o
}

func (o LookupNetworkAclEntryResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupNetworkAclEntryResult] {
	return pulumix.Output[LookupNetworkAclEntryResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupNetworkAclEntryResultOutput) CidrBlock() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkAclEntryResult) *string { return v.CidrBlock }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkAclEntryResultOutput) Icmp() NetworkAclEntryIcmpPtrOutput {
	return o.ApplyT(func(v LookupNetworkAclEntryResult) *NetworkAclEntryIcmp { return v.Icmp }).(NetworkAclEntryIcmpPtrOutput)
}

func (o LookupNetworkAclEntryResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkAclEntryResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkAclEntryResultOutput) Ipv6CidrBlock() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkAclEntryResult) *string { return v.Ipv6CidrBlock }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkAclEntryResultOutput) PortRange() NetworkAclEntryPortRangePtrOutput {
	return o.ApplyT(func(v LookupNetworkAclEntryResult) *NetworkAclEntryPortRange { return v.PortRange }).(NetworkAclEntryPortRangePtrOutput)
}

func (o LookupNetworkAclEntryResultOutput) Protocol() pulumi.IntPtrOutput {
	return o.ApplyT(func(v LookupNetworkAclEntryResult) *int { return v.Protocol }).(pulumi.IntPtrOutput)
}

func (o LookupNetworkAclEntryResultOutput) RuleAction() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkAclEntryResult) *string { return v.RuleAction }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkAclEntryResultOutput{})
}
