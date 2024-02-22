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
func LookupDomain(ctx *pulumi.Context, args *LookupDomainArgs, opts ...pulumi.InvokeOption) (*LookupDomainResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupDomainResult
	err := ctx.Invoke("aws-native:opensearchservice:getDomain", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupDomainArgs struct {
	DomainName string `pulumi:"domainName"`
}

type LookupDomainResult struct {
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpenSearchService::Domain` for more information about the expected schema for this property.
	AccessPolicies              interface{}                          `pulumi:"accessPolicies"`
	AdvancedOptions             map[string]string                    `pulumi:"advancedOptions"`
	AdvancedSecurityOptions     *DomainAdvancedSecurityOptionsInput  `pulumi:"advancedSecurityOptions"`
	Arn                         *string                              `pulumi:"arn"`
	ClusterConfig               *DomainClusterConfig                 `pulumi:"clusterConfig"`
	CognitoOptions              *DomainCognitoOptions                `pulumi:"cognitoOptions"`
	DomainArn                   *string                              `pulumi:"domainArn"`
	DomainEndpoint              *string                              `pulumi:"domainEndpoint"`
	DomainEndpointOptions       *DomainEndpointOptions               `pulumi:"domainEndpointOptions"`
	DomainEndpointV2            *string                              `pulumi:"domainEndpointV2"`
	DomainEndpoints             map[string]string                    `pulumi:"domainEndpoints"`
	EbsOptions                  *DomainEbsOptions                    `pulumi:"ebsOptions"`
	EncryptionAtRestOptions     *DomainEncryptionAtRestOptions       `pulumi:"encryptionAtRestOptions"`
	EngineVersion               *string                              `pulumi:"engineVersion"`
	Id                          *string                              `pulumi:"id"`
	IpAddressType               *string                              `pulumi:"ipAddressType"`
	LogPublishingOptions        map[string]DomainLogPublishingOption `pulumi:"logPublishingOptions"`
	NodeToNodeEncryptionOptions *DomainNodeToNodeEncryptionOptions   `pulumi:"nodeToNodeEncryptionOptions"`
	OffPeakWindowOptions        *DomainOffPeakWindowOptions          `pulumi:"offPeakWindowOptions"`
	ServiceSoftwareOptions      *DomainServiceSoftwareOptions        `pulumi:"serviceSoftwareOptions"`
	SnapshotOptions             *DomainSnapshotOptions               `pulumi:"snapshotOptions"`
	SoftwareUpdateOptions       *DomainSoftwareUpdateOptions         `pulumi:"softwareUpdateOptions"`
	// An arbitrary set of tags (key-value pairs) for this Domain.
	Tags       []aws.Tag         `pulumi:"tags"`
	VpcOptions *DomainVpcOptions `pulumi:"vpcOptions"`
}

func LookupDomainOutput(ctx *pulumi.Context, args LookupDomainOutputArgs, opts ...pulumi.InvokeOption) LookupDomainResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupDomainResult, error) {
			args := v.(LookupDomainArgs)
			r, err := LookupDomain(ctx, &args, opts...)
			var s LookupDomainResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupDomainResultOutput)
}

type LookupDomainOutputArgs struct {
	DomainName pulumi.StringInput `pulumi:"domainName"`
}

func (LookupDomainOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDomainArgs)(nil)).Elem()
}

type LookupDomainResultOutput struct{ *pulumi.OutputState }

func (LookupDomainResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupDomainResult)(nil)).Elem()
}

func (o LookupDomainResultOutput) ToLookupDomainResultOutput() LookupDomainResultOutput {
	return o
}

func (o LookupDomainResultOutput) ToLookupDomainResultOutputWithContext(ctx context.Context) LookupDomainResultOutput {
	return o
}

// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::OpenSearchService::Domain` for more information about the expected schema for this property.
func (o LookupDomainResultOutput) AccessPolicies() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupDomainResult) interface{} { return v.AccessPolicies }).(pulumi.AnyOutput)
}

func (o LookupDomainResultOutput) AdvancedOptions() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupDomainResult) map[string]string { return v.AdvancedOptions }).(pulumi.StringMapOutput)
}

func (o LookupDomainResultOutput) AdvancedSecurityOptions() DomainAdvancedSecurityOptionsInputPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainAdvancedSecurityOptionsInput { return v.AdvancedSecurityOptions }).(DomainAdvancedSecurityOptionsInputPtrOutput)
}

func (o LookupDomainResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupDomainResultOutput) ClusterConfig() DomainClusterConfigPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainClusterConfig { return v.ClusterConfig }).(DomainClusterConfigPtrOutput)
}

func (o LookupDomainResultOutput) CognitoOptions() DomainCognitoOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainCognitoOptions { return v.CognitoOptions }).(DomainCognitoOptionsPtrOutput)
}

func (o LookupDomainResultOutput) DomainArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *string { return v.DomainArn }).(pulumi.StringPtrOutput)
}

func (o LookupDomainResultOutput) DomainEndpoint() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *string { return v.DomainEndpoint }).(pulumi.StringPtrOutput)
}

func (o LookupDomainResultOutput) DomainEndpointOptions() DomainEndpointOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainEndpointOptions { return v.DomainEndpointOptions }).(DomainEndpointOptionsPtrOutput)
}

func (o LookupDomainResultOutput) DomainEndpointV2() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *string { return v.DomainEndpointV2 }).(pulumi.StringPtrOutput)
}

func (o LookupDomainResultOutput) DomainEndpoints() pulumi.StringMapOutput {
	return o.ApplyT(func(v LookupDomainResult) map[string]string { return v.DomainEndpoints }).(pulumi.StringMapOutput)
}

func (o LookupDomainResultOutput) EbsOptions() DomainEbsOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainEbsOptions { return v.EbsOptions }).(DomainEbsOptionsPtrOutput)
}

func (o LookupDomainResultOutput) EncryptionAtRestOptions() DomainEncryptionAtRestOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainEncryptionAtRestOptions { return v.EncryptionAtRestOptions }).(DomainEncryptionAtRestOptionsPtrOutput)
}

func (o LookupDomainResultOutput) EngineVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *string { return v.EngineVersion }).(pulumi.StringPtrOutput)
}

func (o LookupDomainResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

func (o LookupDomainResultOutput) IpAddressType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *string { return v.IpAddressType }).(pulumi.StringPtrOutput)
}

func (o LookupDomainResultOutput) LogPublishingOptions() DomainLogPublishingOptionMapOutput {
	return o.ApplyT(func(v LookupDomainResult) map[string]DomainLogPublishingOption { return v.LogPublishingOptions }).(DomainLogPublishingOptionMapOutput)
}

func (o LookupDomainResultOutput) NodeToNodeEncryptionOptions() DomainNodeToNodeEncryptionOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainNodeToNodeEncryptionOptions { return v.NodeToNodeEncryptionOptions }).(DomainNodeToNodeEncryptionOptionsPtrOutput)
}

func (o LookupDomainResultOutput) OffPeakWindowOptions() DomainOffPeakWindowOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainOffPeakWindowOptions { return v.OffPeakWindowOptions }).(DomainOffPeakWindowOptionsPtrOutput)
}

func (o LookupDomainResultOutput) ServiceSoftwareOptions() DomainServiceSoftwareOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainServiceSoftwareOptions { return v.ServiceSoftwareOptions }).(DomainServiceSoftwareOptionsPtrOutput)
}

func (o LookupDomainResultOutput) SnapshotOptions() DomainSnapshotOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainSnapshotOptions { return v.SnapshotOptions }).(DomainSnapshotOptionsPtrOutput)
}

func (o LookupDomainResultOutput) SoftwareUpdateOptions() DomainSoftwareUpdateOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainSoftwareUpdateOptions { return v.SoftwareUpdateOptions }).(DomainSoftwareUpdateOptionsPtrOutput)
}

// An arbitrary set of tags (key-value pairs) for this Domain.
func (o LookupDomainResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupDomainResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func (o LookupDomainResultOutput) VpcOptions() DomainVpcOptionsPtrOutput {
	return o.ApplyT(func(v LookupDomainResult) *DomainVpcOptions { return v.VpcOptions }).(DomainVpcOptionsPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupDomainResultOutput{})
}
