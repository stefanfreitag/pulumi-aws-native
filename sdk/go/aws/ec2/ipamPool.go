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

// Resource Schema of AWS::EC2::IPAMPool Type
type IpamPool struct {
	pulumi.CustomResourceState

	// The address family of the address space in this pool. Either IPv4 or IPv6.
	AddressFamily pulumi.StringOutput `pulumi:"addressFamily"`
	// The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.
	AllocationDefaultNetmaskLength pulumi.IntPtrOutput `pulumi:"allocationDefaultNetmaskLength"`
	// The maximum allowed netmask length for allocations made from this pool.
	AllocationMaxNetmaskLength pulumi.IntPtrOutput `pulumi:"allocationMaxNetmaskLength"`
	// The minimum allowed netmask length for allocations made from this pool.
	AllocationMinNetmaskLength pulumi.IntPtrOutput `pulumi:"allocationMinNetmaskLength"`
	// When specified, an allocation will not be allowed unless a resource has a matching set of tags.
	AllocationResourceTags IpamPoolTagArrayOutput `pulumi:"allocationResourceTags"`
	// The Amazon Resource Name (ARN) of the IPAM Pool.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.
	AutoImport pulumi.BoolPtrOutput `pulumi:"autoImport"`
	// Limits which service in Amazon Web Services that the pool can be used in.
	AwsService  IpamPoolAwsServicePtrOutput `pulumi:"awsService"`
	Description pulumi.StringPtrOutput      `pulumi:"description"`
	// The Amazon Resource Name (ARN) of the IPAM this pool is a part of.
	IpamArn pulumi.StringOutput `pulumi:"ipamArn"`
	// Id of the IPAM Pool.
	IpamPoolId pulumi.StringOutput `pulumi:"ipamPoolId"`
	// The Amazon Resource Name (ARN) of the scope this pool is a part of.
	IpamScopeArn pulumi.StringOutput `pulumi:"ipamScopeArn"`
	// The Id of the scope this pool is a part of.
	IpamScopeId pulumi.StringOutput `pulumi:"ipamScopeId"`
	// Determines whether this scope contains publicly routable space or space for a private network
	IpamScopeType IpamPoolIpamScopeTypeOutput `pulumi:"ipamScopeType"`
	// The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.
	Locale pulumi.StringPtrOutput `pulumi:"locale"`
	// The depth of this pool in the source pool hierarchy.
	PoolDepth pulumi.IntOutput `pulumi:"poolDepth"`
	// A list of cidrs representing the address space available for allocation in this pool.
	ProvisionedCidrs IpamPoolProvisionedCidrArrayOutput `pulumi:"provisionedCidrs"`
	// The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.
	PublicIpSource IpamPoolPublicIpSourcePtrOutput `pulumi:"publicIpSource"`
	// Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
	PubliclyAdvertisable pulumi.BoolPtrOutput `pulumi:"publiclyAdvertisable"`
	// The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.
	SourceIpamPoolId pulumi.StringPtrOutput          `pulumi:"sourceIpamPoolId"`
	SourceResource   IpamPoolSourceResourcePtrOutput `pulumi:"sourceResource"`
	// The state of this pool. This can be one of the following values: "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", or "delete-complete"
	State IpamPoolStateEnumOutput `pulumi:"state"`
	// An explanation of how the pool arrived at it current state.
	StateMessage pulumi.StringOutput `pulumi:"stateMessage"`
	// An array of key-value pairs to apply to this resource.
	Tags IpamPoolTagArrayOutput `pulumi:"tags"`
}

// NewIpamPool registers a new resource with the given unique name, arguments, and options.
func NewIpamPool(ctx *pulumi.Context,
	name string, args *IpamPoolArgs, opts ...pulumi.ResourceOption) (*IpamPool, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AddressFamily == nil {
		return nil, errors.New("invalid value for required argument 'AddressFamily'")
	}
	if args.IpamScopeId == nil {
		return nil, errors.New("invalid value for required argument 'IpamScopeId'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"addressFamily",
		"awsService",
		"ipamScopeId",
		"locale",
		"publicIpSource",
		"publiclyAdvertisable",
		"sourceIpamPoolId",
		"sourceResource",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource IpamPool
	err := ctx.RegisterResource("aws-native:ec2:IpamPool", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIpamPool gets an existing IpamPool resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIpamPool(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IpamPoolState, opts ...pulumi.ResourceOption) (*IpamPool, error) {
	var resource IpamPool
	err := ctx.ReadResource("aws-native:ec2:IpamPool", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IpamPool resources.
type ipamPoolState struct {
}

type IpamPoolState struct {
}

func (IpamPoolState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipamPoolState)(nil)).Elem()
}

type ipamPoolArgs struct {
	// The address family of the address space in this pool. Either IPv4 or IPv6.
	AddressFamily string `pulumi:"addressFamily"`
	// The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.
	AllocationDefaultNetmaskLength *int `pulumi:"allocationDefaultNetmaskLength"`
	// The maximum allowed netmask length for allocations made from this pool.
	AllocationMaxNetmaskLength *int `pulumi:"allocationMaxNetmaskLength"`
	// The minimum allowed netmask length for allocations made from this pool.
	AllocationMinNetmaskLength *int `pulumi:"allocationMinNetmaskLength"`
	// When specified, an allocation will not be allowed unless a resource has a matching set of tags.
	AllocationResourceTags []IpamPoolTag `pulumi:"allocationResourceTags"`
	// Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.
	AutoImport *bool `pulumi:"autoImport"`
	// Limits which service in Amazon Web Services that the pool can be used in.
	AwsService  *IpamPoolAwsService `pulumi:"awsService"`
	Description *string             `pulumi:"description"`
	// The Id of the scope this pool is a part of.
	IpamScopeId string `pulumi:"ipamScopeId"`
	// The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.
	Locale *string `pulumi:"locale"`
	// A list of cidrs representing the address space available for allocation in this pool.
	ProvisionedCidrs []IpamPoolProvisionedCidr `pulumi:"provisionedCidrs"`
	// The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.
	PublicIpSource *IpamPoolPublicIpSource `pulumi:"publicIpSource"`
	// Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
	PubliclyAdvertisable *bool `pulumi:"publiclyAdvertisable"`
	// The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.
	SourceIpamPoolId *string                 `pulumi:"sourceIpamPoolId"`
	SourceResource   *IpamPoolSourceResource `pulumi:"sourceResource"`
	// An array of key-value pairs to apply to this resource.
	Tags []IpamPoolTag `pulumi:"tags"`
}

// The set of arguments for constructing a IpamPool resource.
type IpamPoolArgs struct {
	// The address family of the address space in this pool. Either IPv4 or IPv6.
	AddressFamily pulumi.StringInput
	// The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.
	AllocationDefaultNetmaskLength pulumi.IntPtrInput
	// The maximum allowed netmask length for allocations made from this pool.
	AllocationMaxNetmaskLength pulumi.IntPtrInput
	// The minimum allowed netmask length for allocations made from this pool.
	AllocationMinNetmaskLength pulumi.IntPtrInput
	// When specified, an allocation will not be allowed unless a resource has a matching set of tags.
	AllocationResourceTags IpamPoolTagArrayInput
	// Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.
	AutoImport pulumi.BoolPtrInput
	// Limits which service in Amazon Web Services that the pool can be used in.
	AwsService  IpamPoolAwsServicePtrInput
	Description pulumi.StringPtrInput
	// The Id of the scope this pool is a part of.
	IpamScopeId pulumi.StringInput
	// The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.
	Locale pulumi.StringPtrInput
	// A list of cidrs representing the address space available for allocation in this pool.
	ProvisionedCidrs IpamPoolProvisionedCidrArrayInput
	// The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.
	PublicIpSource IpamPoolPublicIpSourcePtrInput
	// Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
	PubliclyAdvertisable pulumi.BoolPtrInput
	// The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.
	SourceIpamPoolId pulumi.StringPtrInput
	SourceResource   IpamPoolSourceResourcePtrInput
	// An array of key-value pairs to apply to this resource.
	Tags IpamPoolTagArrayInput
}

func (IpamPoolArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipamPoolArgs)(nil)).Elem()
}

type IpamPoolInput interface {
	pulumi.Input

	ToIpamPoolOutput() IpamPoolOutput
	ToIpamPoolOutputWithContext(ctx context.Context) IpamPoolOutput
}

func (*IpamPool) ElementType() reflect.Type {
	return reflect.TypeOf((**IpamPool)(nil)).Elem()
}

func (i *IpamPool) ToIpamPoolOutput() IpamPoolOutput {
	return i.ToIpamPoolOutputWithContext(context.Background())
}

func (i *IpamPool) ToIpamPoolOutputWithContext(ctx context.Context) IpamPoolOutput {
	return pulumi.ToOutputWithContext(ctx, i).(IpamPoolOutput)
}

func (i *IpamPool) ToOutput(ctx context.Context) pulumix.Output[*IpamPool] {
	return pulumix.Output[*IpamPool]{
		OutputState: i.ToIpamPoolOutputWithContext(ctx).OutputState,
	}
}

type IpamPoolOutput struct{ *pulumi.OutputState }

func (IpamPoolOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**IpamPool)(nil)).Elem()
}

func (o IpamPoolOutput) ToIpamPoolOutput() IpamPoolOutput {
	return o
}

func (o IpamPoolOutput) ToIpamPoolOutputWithContext(ctx context.Context) IpamPoolOutput {
	return o
}

func (o IpamPoolOutput) ToOutput(ctx context.Context) pulumix.Output[*IpamPool] {
	return pulumix.Output[*IpamPool]{
		OutputState: o.OutputState,
	}
}

// The address family of the address space in this pool. Either IPv4 or IPv6.
func (o IpamPoolOutput) AddressFamily() pulumi.StringOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringOutput { return v.AddressFamily }).(pulumi.StringOutput)
}

// The default netmask length for allocations made from this pool. This value is used when the netmask length of an allocation isn't specified.
func (o IpamPoolOutput) AllocationDefaultNetmaskLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.IntPtrOutput { return v.AllocationDefaultNetmaskLength }).(pulumi.IntPtrOutput)
}

// The maximum allowed netmask length for allocations made from this pool.
func (o IpamPoolOutput) AllocationMaxNetmaskLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.IntPtrOutput { return v.AllocationMaxNetmaskLength }).(pulumi.IntPtrOutput)
}

// The minimum allowed netmask length for allocations made from this pool.
func (o IpamPoolOutput) AllocationMinNetmaskLength() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.IntPtrOutput { return v.AllocationMinNetmaskLength }).(pulumi.IntPtrOutput)
}

// When specified, an allocation will not be allowed unless a resource has a matching set of tags.
func (o IpamPoolOutput) AllocationResourceTags() IpamPoolTagArrayOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolTagArrayOutput { return v.AllocationResourceTags }).(IpamPoolTagArrayOutput)
}

// The Amazon Resource Name (ARN) of the IPAM Pool.
func (o IpamPoolOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

// Determines what to do if IPAM discovers resources that haven't been assigned an allocation. If set to true, an allocation will be made automatically.
func (o IpamPoolOutput) AutoImport() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.BoolPtrOutput { return v.AutoImport }).(pulumi.BoolPtrOutput)
}

// Limits which service in Amazon Web Services that the pool can be used in.
func (o IpamPoolOutput) AwsService() IpamPoolAwsServicePtrOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolAwsServicePtrOutput { return v.AwsService }).(IpamPoolAwsServicePtrOutput)
}

func (o IpamPoolOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

// The Amazon Resource Name (ARN) of the IPAM this pool is a part of.
func (o IpamPoolOutput) IpamArn() pulumi.StringOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringOutput { return v.IpamArn }).(pulumi.StringOutput)
}

// Id of the IPAM Pool.
func (o IpamPoolOutput) IpamPoolId() pulumi.StringOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringOutput { return v.IpamPoolId }).(pulumi.StringOutput)
}

// The Amazon Resource Name (ARN) of the scope this pool is a part of.
func (o IpamPoolOutput) IpamScopeArn() pulumi.StringOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringOutput { return v.IpamScopeArn }).(pulumi.StringOutput)
}

// The Id of the scope this pool is a part of.
func (o IpamPoolOutput) IpamScopeId() pulumi.StringOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringOutput { return v.IpamScopeId }).(pulumi.StringOutput)
}

// Determines whether this scope contains publicly routable space or space for a private network
func (o IpamPoolOutput) IpamScopeType() IpamPoolIpamScopeTypeOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolIpamScopeTypeOutput { return v.IpamScopeType }).(IpamPoolIpamScopeTypeOutput)
}

// The region of this pool. If not set, this will default to "None" which will disable non-custom allocations. If the locale has been specified for the source pool, this value must match.
func (o IpamPoolOutput) Locale() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringPtrOutput { return v.Locale }).(pulumi.StringPtrOutput)
}

// The depth of this pool in the source pool hierarchy.
func (o IpamPoolOutput) PoolDepth() pulumi.IntOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.IntOutput { return v.PoolDepth }).(pulumi.IntOutput)
}

// A list of cidrs representing the address space available for allocation in this pool.
func (o IpamPoolOutput) ProvisionedCidrs() IpamPoolProvisionedCidrArrayOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolProvisionedCidrArrayOutput { return v.ProvisionedCidrs }).(IpamPoolProvisionedCidrArrayOutput)
}

// The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.
func (o IpamPoolOutput) PublicIpSource() IpamPoolPublicIpSourcePtrOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolPublicIpSourcePtrOutput { return v.PublicIpSource }).(IpamPoolPublicIpSourcePtrOutput)
}

// Determines whether or not address space from this pool is publicly advertised. Must be set if and only if the pool is IPv6.
func (o IpamPoolOutput) PubliclyAdvertisable() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.BoolPtrOutput { return v.PubliclyAdvertisable }).(pulumi.BoolPtrOutput)
}

// The Id of this pool's source. If set, all space provisioned in this pool must be free space provisioned in the parent pool.
func (o IpamPoolOutput) SourceIpamPoolId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringPtrOutput { return v.SourceIpamPoolId }).(pulumi.StringPtrOutput)
}

func (o IpamPoolOutput) SourceResource() IpamPoolSourceResourcePtrOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolSourceResourcePtrOutput { return v.SourceResource }).(IpamPoolSourceResourcePtrOutput)
}

// The state of this pool. This can be one of the following values: "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", or "delete-complete"
func (o IpamPoolOutput) State() IpamPoolStateEnumOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolStateEnumOutput { return v.State }).(IpamPoolStateEnumOutput)
}

// An explanation of how the pool arrived at it current state.
func (o IpamPoolOutput) StateMessage() pulumi.StringOutput {
	return o.ApplyT(func(v *IpamPool) pulumi.StringOutput { return v.StateMessage }).(pulumi.StringOutput)
}

// An array of key-value pairs to apply to this resource.
func (o IpamPoolOutput) Tags() IpamPoolTagArrayOutput {
	return o.ApplyT(func(v *IpamPool) IpamPoolTagArrayOutput { return v.Tags }).(IpamPoolTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*IpamPoolInput)(nil)).Elem(), &IpamPool{})
	pulumi.RegisterOutputType(IpamPoolOutput{})
}
