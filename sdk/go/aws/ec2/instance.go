// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::EC2::Instance
//
// Deprecated: Instance is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Instance struct {
	pulumi.CustomResourceState

	AdditionalInfo                    pulumi.StringPtrOutput                         `pulumi:"additionalInfo"`
	Affinity                          pulumi.StringPtrOutput                         `pulumi:"affinity"`
	AvailabilityZone                  pulumi.StringPtrOutput                         `pulumi:"availabilityZone"`
	BlockDeviceMappings               InstanceBlockDeviceMappingArrayOutput          `pulumi:"blockDeviceMappings"`
	CpuOptions                        InstanceCpuOptionsPtrOutput                    `pulumi:"cpuOptions"`
	CreditSpecification               InstanceCreditSpecificationPtrOutput           `pulumi:"creditSpecification"`
	DisableApiTermination             pulumi.BoolPtrOutput                           `pulumi:"disableApiTermination"`
	EbsOptimized                      pulumi.BoolPtrOutput                           `pulumi:"ebsOptimized"`
	ElasticGpuSpecifications          InstanceElasticGpuSpecificationArrayOutput     `pulumi:"elasticGpuSpecifications"`
	ElasticInferenceAccelerators      InstanceElasticInferenceAcceleratorArrayOutput `pulumi:"elasticInferenceAccelerators"`
	EnclaveOptions                    InstanceEnclaveOptionsPtrOutput                `pulumi:"enclaveOptions"`
	HibernationOptions                InstanceHibernationOptionsPtrOutput            `pulumi:"hibernationOptions"`
	HostId                            pulumi.StringPtrOutput                         `pulumi:"hostId"`
	HostResourceGroupArn              pulumi.StringPtrOutput                         `pulumi:"hostResourceGroupArn"`
	IamInstanceProfile                pulumi.StringPtrOutput                         `pulumi:"iamInstanceProfile"`
	ImageId                           pulumi.StringPtrOutput                         `pulumi:"imageId"`
	InstanceInitiatedShutdownBehavior pulumi.StringPtrOutput                         `pulumi:"instanceInitiatedShutdownBehavior"`
	InstanceType                      pulumi.StringPtrOutput                         `pulumi:"instanceType"`
	Ipv6AddressCount                  pulumi.IntPtrOutput                            `pulumi:"ipv6AddressCount"`
	Ipv6Addresses                     InstanceIpv6AddressArrayOutput                 `pulumi:"ipv6Addresses"`
	KernelId                          pulumi.StringPtrOutput                         `pulumi:"kernelId"`
	KeyName                           pulumi.StringPtrOutput                         `pulumi:"keyName"`
	LaunchTemplate                    InstanceLaunchTemplateSpecificationPtrOutput   `pulumi:"launchTemplate"`
	LicenseSpecifications             InstanceLicenseSpecificationArrayOutput        `pulumi:"licenseSpecifications"`
	Monitoring                        pulumi.BoolPtrOutput                           `pulumi:"monitoring"`
	NetworkInterfaces                 InstanceNetworkInterfaceArrayOutput            `pulumi:"networkInterfaces"`
	PlacementGroupName                pulumi.StringPtrOutput                         `pulumi:"placementGroupName"`
	PrivateDnsName                    pulumi.StringOutput                            `pulumi:"privateDnsName"`
	PrivateIp                         pulumi.StringOutput                            `pulumi:"privateIp"`
	PrivateIpAddress                  pulumi.StringPtrOutput                         `pulumi:"privateIpAddress"`
	PublicDnsName                     pulumi.StringOutput                            `pulumi:"publicDnsName"`
	PublicIp                          pulumi.StringOutput                            `pulumi:"publicIp"`
	RamdiskId                         pulumi.StringPtrOutput                         `pulumi:"ramdiskId"`
	SecurityGroupIds                  pulumi.StringArrayOutput                       `pulumi:"securityGroupIds"`
	SecurityGroups                    pulumi.StringArrayOutput                       `pulumi:"securityGroups"`
	SourceDestCheck                   pulumi.BoolPtrOutput                           `pulumi:"sourceDestCheck"`
	SsmAssociations                   InstanceSsmAssociationArrayOutput              `pulumi:"ssmAssociations"`
	SubnetId                          pulumi.StringPtrOutput                         `pulumi:"subnetId"`
	Tags                              InstanceTagArrayOutput                         `pulumi:"tags"`
	Tenancy                           pulumi.StringPtrOutput                         `pulumi:"tenancy"`
	UserData                          pulumi.StringPtrOutput                         `pulumi:"userData"`
	Volumes                           InstanceVolumeArrayOutput                      `pulumi:"volumes"`
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOption) (*Instance, error) {
	if args == nil {
		args = &InstanceArgs{}
	}

	var resource Instance
	err := ctx.RegisterResource("aws-native:ec2:Instance", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *InstanceState, opts ...pulumi.ResourceOption) (*Instance, error) {
	var resource Instance
	err := ctx.ReadResource("aws-native:ec2:Instance", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Instance resources.
type instanceState struct {
}

type InstanceState struct {
}

func (InstanceState) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceState)(nil)).Elem()
}

type instanceArgs struct {
	AdditionalInfo                    *string                               `pulumi:"additionalInfo"`
	Affinity                          *string                               `pulumi:"affinity"`
	AvailabilityZone                  *string                               `pulumi:"availabilityZone"`
	BlockDeviceMappings               []InstanceBlockDeviceMapping          `pulumi:"blockDeviceMappings"`
	CpuOptions                        *InstanceCpuOptions                   `pulumi:"cpuOptions"`
	CreditSpecification               *InstanceCreditSpecification          `pulumi:"creditSpecification"`
	DisableApiTermination             *bool                                 `pulumi:"disableApiTermination"`
	EbsOptimized                      *bool                                 `pulumi:"ebsOptimized"`
	ElasticGpuSpecifications          []InstanceElasticGpuSpecification     `pulumi:"elasticGpuSpecifications"`
	ElasticInferenceAccelerators      []InstanceElasticInferenceAccelerator `pulumi:"elasticInferenceAccelerators"`
	EnclaveOptions                    *InstanceEnclaveOptions               `pulumi:"enclaveOptions"`
	HibernationOptions                *InstanceHibernationOptions           `pulumi:"hibernationOptions"`
	HostId                            *string                               `pulumi:"hostId"`
	HostResourceGroupArn              *string                               `pulumi:"hostResourceGroupArn"`
	IamInstanceProfile                *string                               `pulumi:"iamInstanceProfile"`
	ImageId                           *string                               `pulumi:"imageId"`
	InstanceInitiatedShutdownBehavior *string                               `pulumi:"instanceInitiatedShutdownBehavior"`
	InstanceType                      *string                               `pulumi:"instanceType"`
	Ipv6AddressCount                  *int                                  `pulumi:"ipv6AddressCount"`
	Ipv6Addresses                     []InstanceIpv6Address                 `pulumi:"ipv6Addresses"`
	KernelId                          *string                               `pulumi:"kernelId"`
	KeyName                           *string                               `pulumi:"keyName"`
	LaunchTemplate                    *InstanceLaunchTemplateSpecification  `pulumi:"launchTemplate"`
	LicenseSpecifications             []InstanceLicenseSpecification        `pulumi:"licenseSpecifications"`
	Monitoring                        *bool                                 `pulumi:"monitoring"`
	NetworkInterfaces                 []InstanceNetworkInterface            `pulumi:"networkInterfaces"`
	PlacementGroupName                *string                               `pulumi:"placementGroupName"`
	PrivateIpAddress                  *string                               `pulumi:"privateIpAddress"`
	RamdiskId                         *string                               `pulumi:"ramdiskId"`
	SecurityGroupIds                  []string                              `pulumi:"securityGroupIds"`
	SecurityGroups                    []string                              `pulumi:"securityGroups"`
	SourceDestCheck                   *bool                                 `pulumi:"sourceDestCheck"`
	SsmAssociations                   []InstanceSsmAssociation              `pulumi:"ssmAssociations"`
	SubnetId                          *string                               `pulumi:"subnetId"`
	Tags                              []InstanceTag                         `pulumi:"tags"`
	Tenancy                           *string                               `pulumi:"tenancy"`
	UserData                          *string                               `pulumi:"userData"`
	Volumes                           []InstanceVolume                      `pulumi:"volumes"`
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	AdditionalInfo                    pulumi.StringPtrInput
	Affinity                          pulumi.StringPtrInput
	AvailabilityZone                  pulumi.StringPtrInput
	BlockDeviceMappings               InstanceBlockDeviceMappingArrayInput
	CpuOptions                        InstanceCpuOptionsPtrInput
	CreditSpecification               InstanceCreditSpecificationPtrInput
	DisableApiTermination             pulumi.BoolPtrInput
	EbsOptimized                      pulumi.BoolPtrInput
	ElasticGpuSpecifications          InstanceElasticGpuSpecificationArrayInput
	ElasticInferenceAccelerators      InstanceElasticInferenceAcceleratorArrayInput
	EnclaveOptions                    InstanceEnclaveOptionsPtrInput
	HibernationOptions                InstanceHibernationOptionsPtrInput
	HostId                            pulumi.StringPtrInput
	HostResourceGroupArn              pulumi.StringPtrInput
	IamInstanceProfile                pulumi.StringPtrInput
	ImageId                           pulumi.StringPtrInput
	InstanceInitiatedShutdownBehavior pulumi.StringPtrInput
	InstanceType                      pulumi.StringPtrInput
	Ipv6AddressCount                  pulumi.IntPtrInput
	Ipv6Addresses                     InstanceIpv6AddressArrayInput
	KernelId                          pulumi.StringPtrInput
	KeyName                           pulumi.StringPtrInput
	LaunchTemplate                    InstanceLaunchTemplateSpecificationPtrInput
	LicenseSpecifications             InstanceLicenseSpecificationArrayInput
	Monitoring                        pulumi.BoolPtrInput
	NetworkInterfaces                 InstanceNetworkInterfaceArrayInput
	PlacementGroupName                pulumi.StringPtrInput
	PrivateIpAddress                  pulumi.StringPtrInput
	RamdiskId                         pulumi.StringPtrInput
	SecurityGroupIds                  pulumi.StringArrayInput
	SecurityGroups                    pulumi.StringArrayInput
	SourceDestCheck                   pulumi.BoolPtrInput
	SsmAssociations                   InstanceSsmAssociationArrayInput
	SubnetId                          pulumi.StringPtrInput
	Tags                              InstanceTagArrayInput
	Tenancy                           pulumi.StringPtrInput
	UserData                          pulumi.StringPtrInput
	Volumes                           InstanceVolumeArrayInput
}

func (InstanceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*instanceArgs)(nil)).Elem()
}

type InstanceInput interface {
	pulumi.Input

	ToInstanceOutput() InstanceOutput
	ToInstanceOutputWithContext(ctx context.Context) InstanceOutput
}

func (*Instance) ElementType() reflect.Type {
	return reflect.TypeOf((*Instance)(nil))
}

func (i *Instance) ToInstanceOutput() InstanceOutput {
	return i.ToInstanceOutputWithContext(context.Background())
}

func (i *Instance) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(InstanceOutput)
}

type InstanceOutput struct{ *pulumi.OutputState }

func (InstanceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Instance)(nil))
}

func (o InstanceOutput) ToInstanceOutput() InstanceOutput {
	return o
}

func (o InstanceOutput) ToInstanceOutputWithContext(ctx context.Context) InstanceOutput {
	return o
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*InstanceInput)(nil)).Elem(), &Instance{})
	pulumi.RegisterOutputType(InstanceOutput{})
}
