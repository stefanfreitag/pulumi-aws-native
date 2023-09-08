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

// Resource Schema of AWS::EC2::IPAMResourceDiscovery Type
func LookupIpamResourceDiscovery(ctx *pulumi.Context, args *LookupIpamResourceDiscoveryArgs, opts ...pulumi.InvokeOption) (*LookupIpamResourceDiscoveryResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupIpamResourceDiscoveryResult
	err := ctx.Invoke("aws-native:ec2:getIpamResourceDiscovery", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupIpamResourceDiscoveryArgs struct {
	// Id of the IPAM Pool.
	IpamResourceDiscoveryId string `pulumi:"ipamResourceDiscoveryId"`
}

type LookupIpamResourceDiscoveryResult struct {
	Description *string `pulumi:"description"`
	// Amazon Resource Name (Arn) for the Resource Discovery.
	IpamResourceDiscoveryArn *string `pulumi:"ipamResourceDiscoveryArn"`
	// Id of the IPAM Pool.
	IpamResourceDiscoveryId *string `pulumi:"ipamResourceDiscoveryId"`
	// The region the resource discovery is setup in.
	IpamResourceDiscoveryRegion *string `pulumi:"ipamResourceDiscoveryRegion"`
	// Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
	IsDefault *bool `pulumi:"isDefault"`
	// The regions Resource Discovery is enabled for. Allows resource discoveries to be created in these regions, as well as enabling monitoring
	OperatingRegions []IpamResourceDiscoveryIpamOperatingRegion `pulumi:"operatingRegions"`
	// Owner Account ID of the Resource Discovery
	OwnerId *string `pulumi:"ownerId"`
	// The state of this Resource Discovery.
	State *string `pulumi:"state"`
	// An array of key-value pairs to apply to this resource.
	Tags []IpamResourceDiscoveryTag `pulumi:"tags"`
}

func LookupIpamResourceDiscoveryOutput(ctx *pulumi.Context, args LookupIpamResourceDiscoveryOutputArgs, opts ...pulumi.InvokeOption) LookupIpamResourceDiscoveryResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupIpamResourceDiscoveryResult, error) {
			args := v.(LookupIpamResourceDiscoveryArgs)
			r, err := LookupIpamResourceDiscovery(ctx, &args, opts...)
			var s LookupIpamResourceDiscoveryResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupIpamResourceDiscoveryResultOutput)
}

type LookupIpamResourceDiscoveryOutputArgs struct {
	// Id of the IPAM Pool.
	IpamResourceDiscoveryId pulumi.StringInput `pulumi:"ipamResourceDiscoveryId"`
}

func (LookupIpamResourceDiscoveryOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpamResourceDiscoveryArgs)(nil)).Elem()
}

type LookupIpamResourceDiscoveryResultOutput struct{ *pulumi.OutputState }

func (LookupIpamResourceDiscoveryResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupIpamResourceDiscoveryResult)(nil)).Elem()
}

func (o LookupIpamResourceDiscoveryResultOutput) ToLookupIpamResourceDiscoveryResultOutput() LookupIpamResourceDiscoveryResultOutput {
	return o
}

func (o LookupIpamResourceDiscoveryResultOutput) ToLookupIpamResourceDiscoveryResultOutputWithContext(ctx context.Context) LookupIpamResourceDiscoveryResultOutput {
	return o
}

func (o LookupIpamResourceDiscoveryResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupIpamResourceDiscoveryResult] {
	return pulumix.Output[LookupIpamResourceDiscoveryResult]{
		OutputState: o.OutputState,
	}
}

func (o LookupIpamResourceDiscoveryResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Amazon Resource Name (Arn) for the Resource Discovery.
func (o LookupIpamResourceDiscoveryResultOutput) IpamResourceDiscoveryArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) *string { return v.IpamResourceDiscoveryArn }).(pulumi.StringPtrOutput)
}

// Id of the IPAM Pool.
func (o LookupIpamResourceDiscoveryResultOutput) IpamResourceDiscoveryId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) *string { return v.IpamResourceDiscoveryId }).(pulumi.StringPtrOutput)
}

// The region the resource discovery is setup in.
func (o LookupIpamResourceDiscoveryResultOutput) IpamResourceDiscoveryRegion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) *string { return v.IpamResourceDiscoveryRegion }).(pulumi.StringPtrOutput)
}

// Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
func (o LookupIpamResourceDiscoveryResultOutput) IsDefault() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) *bool { return v.IsDefault }).(pulumi.BoolPtrOutput)
}

// The regions Resource Discovery is enabled for. Allows resource discoveries to be created in these regions, as well as enabling monitoring
func (o LookupIpamResourceDiscoveryResultOutput) OperatingRegions() IpamResourceDiscoveryIpamOperatingRegionArrayOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) []IpamResourceDiscoveryIpamOperatingRegion {
		return v.OperatingRegions
	}).(IpamResourceDiscoveryIpamOperatingRegionArrayOutput)
}

// Owner Account ID of the Resource Discovery
func (o LookupIpamResourceDiscoveryResultOutput) OwnerId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) *string { return v.OwnerId }).(pulumi.StringPtrOutput)
}

// The state of this Resource Discovery.
func (o LookupIpamResourceDiscoveryResultOutput) State() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) *string { return v.State }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupIpamResourceDiscoveryResultOutput) Tags() IpamResourceDiscoveryTagArrayOutput {
	return o.ApplyT(func(v LookupIpamResourceDiscoveryResult) []IpamResourceDiscoveryTag { return v.Tags }).(IpamResourceDiscoveryTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupIpamResourceDiscoveryResultOutput{})
}
