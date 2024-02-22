// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package opensearchservice

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// An example resource schema demonstrating some basic constructs and validation rules.
type Domain struct {
	pulumi.CustomResourceState

	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpenSearchService::Domain` for more information about the expected schema for this property.
	AccessPolicies              pulumi.AnyOutput                            `pulumi:"accessPolicies"`
	AdvancedOptions             pulumi.StringMapOutput                      `pulumi:"advancedOptions"`
	AdvancedSecurityOptions     DomainAdvancedSecurityOptionsInputPtrOutput `pulumi:"advancedSecurityOptions"`
	Arn                         pulumi.StringOutput                         `pulumi:"arn"`
	ClusterConfig               DomainClusterConfigPtrOutput                `pulumi:"clusterConfig"`
	CognitoOptions              DomainCognitoOptionsPtrOutput               `pulumi:"cognitoOptions"`
	DomainArn                   pulumi.StringOutput                         `pulumi:"domainArn"`
	DomainEndpoint              pulumi.StringOutput                         `pulumi:"domainEndpoint"`
	DomainEndpointOptions       DomainEndpointOptionsPtrOutput              `pulumi:"domainEndpointOptions"`
	DomainEndpointV2            pulumi.StringOutput                         `pulumi:"domainEndpointV2"`
	DomainEndpoints             pulumi.StringMapOutput                      `pulumi:"domainEndpoints"`
	DomainName                  pulumi.StringPtrOutput                      `pulumi:"domainName"`
	EbsOptions                  DomainEbsOptionsPtrOutput                   `pulumi:"ebsOptions"`
	EncryptionAtRestOptions     DomainEncryptionAtRestOptionsPtrOutput      `pulumi:"encryptionAtRestOptions"`
	EngineVersion               pulumi.StringPtrOutput                      `pulumi:"engineVersion"`
	IpAddressType               pulumi.StringPtrOutput                      `pulumi:"ipAddressType"`
	LogPublishingOptions        DomainLogPublishingOptionMapOutput          `pulumi:"logPublishingOptions"`
	NodeToNodeEncryptionOptions DomainNodeToNodeEncryptionOptionsPtrOutput  `pulumi:"nodeToNodeEncryptionOptions"`
	OffPeakWindowOptions        DomainOffPeakWindowOptionsPtrOutput         `pulumi:"offPeakWindowOptions"`
	ServiceSoftwareOptions      DomainServiceSoftwareOptionsOutput          `pulumi:"serviceSoftwareOptions"`
	SnapshotOptions             DomainSnapshotOptionsPtrOutput              `pulumi:"snapshotOptions"`
	SoftwareUpdateOptions       DomainSoftwareUpdateOptionsPtrOutput        `pulumi:"softwareUpdateOptions"`
	// An arbitrary set of tags (key-value pairs) for this Domain.
	Tags       aws.TagArrayOutput        `pulumi:"tags"`
	VpcOptions DomainVpcOptionsPtrOutput `pulumi:"vpcOptions"`
}

// NewDomain registers a new resource with the given unique name, arguments, and options.
func NewDomain(ctx *pulumi.Context,
	name string, args *DomainArgs, opts ...pulumi.ResourceOption) (*Domain, error) {
	if args == nil {
		args = &DomainArgs{}
	}

	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"domainName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Domain
	err := ctx.RegisterResource("aws-native:opensearchservice:Domain", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDomain gets an existing Domain resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDomain(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DomainState, opts ...pulumi.ResourceOption) (*Domain, error) {
	var resource Domain
	err := ctx.ReadResource("aws-native:opensearchservice:Domain", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Domain resources.
type domainState struct {
}

type DomainState struct {
}

func (DomainState) ElementType() reflect.Type {
	return reflect.TypeOf((*domainState)(nil)).Elem()
}

type domainArgs struct {
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpenSearchService::Domain` for more information about the expected schema for this property.
	AccessPolicies              interface{}                          `pulumi:"accessPolicies"`
	AdvancedOptions             map[string]string                    `pulumi:"advancedOptions"`
	AdvancedSecurityOptions     *DomainAdvancedSecurityOptionsInput  `pulumi:"advancedSecurityOptions"`
	ClusterConfig               *DomainClusterConfig                 `pulumi:"clusterConfig"`
	CognitoOptions              *DomainCognitoOptions                `pulumi:"cognitoOptions"`
	DomainEndpointOptions       *DomainEndpointOptions               `pulumi:"domainEndpointOptions"`
	DomainName                  *string                              `pulumi:"domainName"`
	EbsOptions                  *DomainEbsOptions                    `pulumi:"ebsOptions"`
	EncryptionAtRestOptions     *DomainEncryptionAtRestOptions       `pulumi:"encryptionAtRestOptions"`
	EngineVersion               *string                              `pulumi:"engineVersion"`
	IpAddressType               *string                              `pulumi:"ipAddressType"`
	LogPublishingOptions        map[string]DomainLogPublishingOption `pulumi:"logPublishingOptions"`
	NodeToNodeEncryptionOptions *DomainNodeToNodeEncryptionOptions   `pulumi:"nodeToNodeEncryptionOptions"`
	OffPeakWindowOptions        *DomainOffPeakWindowOptions          `pulumi:"offPeakWindowOptions"`
	SnapshotOptions             *DomainSnapshotOptions               `pulumi:"snapshotOptions"`
	SoftwareUpdateOptions       *DomainSoftwareUpdateOptions         `pulumi:"softwareUpdateOptions"`
	// An arbitrary set of tags (key-value pairs) for this Domain.
	Tags       []aws.Tag         `pulumi:"tags"`
	VpcOptions *DomainVpcOptions `pulumi:"vpcOptions"`
}

// The set of arguments for constructing a Domain resource.
type DomainArgs struct {
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpenSearchService::Domain` for more information about the expected schema for this property.
	AccessPolicies              pulumi.Input
	AdvancedOptions             pulumi.StringMapInput
	AdvancedSecurityOptions     DomainAdvancedSecurityOptionsInputPtrInput
	ClusterConfig               DomainClusterConfigPtrInput
	CognitoOptions              DomainCognitoOptionsPtrInput
	DomainEndpointOptions       DomainEndpointOptionsPtrInput
	DomainName                  pulumi.StringPtrInput
	EbsOptions                  DomainEbsOptionsPtrInput
	EncryptionAtRestOptions     DomainEncryptionAtRestOptionsPtrInput
	EngineVersion               pulumi.StringPtrInput
	IpAddressType               pulumi.StringPtrInput
	LogPublishingOptions        DomainLogPublishingOptionMapInput
	NodeToNodeEncryptionOptions DomainNodeToNodeEncryptionOptionsPtrInput
	OffPeakWindowOptions        DomainOffPeakWindowOptionsPtrInput
	SnapshotOptions             DomainSnapshotOptionsPtrInput
	SoftwareUpdateOptions       DomainSoftwareUpdateOptionsPtrInput
	// An arbitrary set of tags (key-value pairs) for this Domain.
	Tags       aws.TagArrayInput
	VpcOptions DomainVpcOptionsPtrInput
}

func (DomainArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*domainArgs)(nil)).Elem()
}

type DomainInput interface {
	pulumi.Input

	ToDomainOutput() DomainOutput
	ToDomainOutputWithContext(ctx context.Context) DomainOutput
}

func (*Domain) ElementType() reflect.Type {
	return reflect.TypeOf((**Domain)(nil)).Elem()
}

func (i *Domain) ToDomainOutput() DomainOutput {
	return i.ToDomainOutputWithContext(context.Background())
}

func (i *Domain) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DomainOutput)
}

type DomainOutput struct{ *pulumi.OutputState }

func (DomainOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Domain)(nil)).Elem()
}

func (o DomainOutput) ToDomainOutput() DomainOutput {
	return o
}

func (o DomainOutput) ToDomainOutputWithContext(ctx context.Context) DomainOutput {
	return o
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpenSearchService::Domain` for more information about the expected schema for this property.
func (o DomainOutput) AccessPolicies() pulumi.AnyOutput {
	return o.ApplyT(func(v *Domain) pulumi.AnyOutput { return v.AccessPolicies }).(pulumi.AnyOutput)
}

func (o DomainOutput) AdvancedOptions() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringMapOutput { return v.AdvancedOptions }).(pulumi.StringMapOutput)
}

func (o DomainOutput) AdvancedSecurityOptions() DomainAdvancedSecurityOptionsInputPtrOutput {
	return o.ApplyT(func(v *Domain) DomainAdvancedSecurityOptionsInputPtrOutput { return v.AdvancedSecurityOptions }).(DomainAdvancedSecurityOptionsInputPtrOutput)
}

func (o DomainOutput) Arn() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.Arn }).(pulumi.StringOutput)
}

func (o DomainOutput) ClusterConfig() DomainClusterConfigPtrOutput {
	return o.ApplyT(func(v *Domain) DomainClusterConfigPtrOutput { return v.ClusterConfig }).(DomainClusterConfigPtrOutput)
}

func (o DomainOutput) CognitoOptions() DomainCognitoOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainCognitoOptionsPtrOutput { return v.CognitoOptions }).(DomainCognitoOptionsPtrOutput)
}

func (o DomainOutput) DomainArn() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.DomainArn }).(pulumi.StringOutput)
}

func (o DomainOutput) DomainEndpoint() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.DomainEndpoint }).(pulumi.StringOutput)
}

func (o DomainOutput) DomainEndpointOptions() DomainEndpointOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainEndpointOptionsPtrOutput { return v.DomainEndpointOptions }).(DomainEndpointOptionsPtrOutput)
}

func (o DomainOutput) DomainEndpointV2() pulumi.StringOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringOutput { return v.DomainEndpointV2 }).(pulumi.StringOutput)
}

func (o DomainOutput) DomainEndpoints() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringMapOutput { return v.DomainEndpoints }).(pulumi.StringMapOutput)
}

func (o DomainOutput) DomainName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringPtrOutput { return v.DomainName }).(pulumi.StringPtrOutput)
}

func (o DomainOutput) EbsOptions() DomainEbsOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainEbsOptionsPtrOutput { return v.EbsOptions }).(DomainEbsOptionsPtrOutput)
}

func (o DomainOutput) EncryptionAtRestOptions() DomainEncryptionAtRestOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainEncryptionAtRestOptionsPtrOutput { return v.EncryptionAtRestOptions }).(DomainEncryptionAtRestOptionsPtrOutput)
}

func (o DomainOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringPtrOutput { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

func (o DomainOutput) IpAddressType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Domain) pulumi.StringPtrOutput { return v.IpAddressType }).(pulumi.StringPtrOutput)
}

func (o DomainOutput) LogPublishingOptions() DomainLogPublishingOptionMapOutput {
	return o.ApplyT(func(v *Domain) DomainLogPublishingOptionMapOutput { return v.LogPublishingOptions }).(DomainLogPublishingOptionMapOutput)
}

func (o DomainOutput) NodeToNodeEncryptionOptions() DomainNodeToNodeEncryptionOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainNodeToNodeEncryptionOptionsPtrOutput { return v.NodeToNodeEncryptionOptions }).(DomainNodeToNodeEncryptionOptionsPtrOutput)
}

func (o DomainOutput) OffPeakWindowOptions() DomainOffPeakWindowOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainOffPeakWindowOptionsPtrOutput { return v.OffPeakWindowOptions }).(DomainOffPeakWindowOptionsPtrOutput)
}

func (o DomainOutput) ServiceSoftwareOptions() DomainServiceSoftwareOptionsOutput {
	return o.ApplyT(func(v *Domain) DomainServiceSoftwareOptionsOutput { return v.ServiceSoftwareOptions }).(DomainServiceSoftwareOptionsOutput)
}

func (o DomainOutput) SnapshotOptions() DomainSnapshotOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainSnapshotOptionsPtrOutput { return v.SnapshotOptions }).(DomainSnapshotOptionsPtrOutput)
}

func (o DomainOutput) SoftwareUpdateOptions() DomainSoftwareUpdateOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainSoftwareUpdateOptionsPtrOutput { return v.SoftwareUpdateOptions }).(DomainSoftwareUpdateOptionsPtrOutput)
}

// An arbitrary set of tags (key-value pairs) for this Domain.
func (o DomainOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Domain) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o DomainOutput) VpcOptions() DomainVpcOptionsPtrOutput {
	return o.ApplyT(func(v *Domain) DomainVpcOptionsPtrOutput { return v.VpcOptions }).(DomainVpcOptionsPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DomainInput)(nil)).Elem(), &Domain{})
	pulumi.RegisterOutputType(DomainOutput{})
}
