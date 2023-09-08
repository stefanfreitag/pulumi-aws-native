// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package licensemanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::LicenseManager::License
func LookupLicense(ctx *pulumi.Context, args *LookupLicenseArgs, opts ...pulumi.InvokeOption) (*LookupLicenseResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupLicenseResult
	err := ctx.Invoke("aws-native:licensemanager:getLicense", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupLicenseArgs struct {
	// Amazon Resource Name is a unique name for each resource.
	LicenseArn string `pulumi:"licenseArn"`
}

type LookupLicenseResult struct {
	// Beneficiary of the license.
	Beneficiary              *string                          `pulumi:"beneficiary"`
	ConsumptionConfiguration *LicenseConsumptionConfiguration `pulumi:"consumptionConfiguration"`
	Entitlements             []LicenseEntitlement             `pulumi:"entitlements"`
	// Home region for the created license.
	HomeRegion *string            `pulumi:"homeRegion"`
	Issuer     *LicenseIssuerData `pulumi:"issuer"`
	// Amazon Resource Name is a unique name for each resource.
	LicenseArn      *string           `pulumi:"licenseArn"`
	LicenseMetadata []LicenseMetadata `pulumi:"licenseMetadata"`
	// Name for the created license.
	LicenseName *string `pulumi:"licenseName"`
	// Product name for the created license.
	ProductName *string `pulumi:"productName"`
	// ProductSKU of the license.
	ProductSku *string                    `pulumi:"productSku"`
	Validity   *LicenseValidityDateFormat `pulumi:"validity"`
	// The version of the license.
	Version *string `pulumi:"version"`
}

func LookupLicenseOutput(ctx *pulumi.Context, args LookupLicenseOutputArgs, opts ...pulumi.InvokeOption) LookupLicenseResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupLicenseResult, error) {
			args := v.(LookupLicenseArgs)
			r, err := LookupLicense(ctx, &args, opts...)
			var s LookupLicenseResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupLicenseResultOutput)
}

type LookupLicenseOutputArgs struct {
	// Amazon Resource Name is a unique name for each resource.
	LicenseArn pulumi.StringInput `pulumi:"licenseArn"`
}

func (LookupLicenseOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLicenseArgs)(nil)).Elem()
}

type LookupLicenseResultOutput struct{ *pulumi.OutputState }

func (LookupLicenseResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupLicenseResult)(nil)).Elem()
}

func (o LookupLicenseResultOutput) ToLookupLicenseResultOutput() LookupLicenseResultOutput {
	return o
}

func (o LookupLicenseResultOutput) ToLookupLicenseResultOutputWithContext(ctx context.Context) LookupLicenseResultOutput {
	return o
}

func (o LookupLicenseResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupLicenseResult] {
	return pulumix.Output[LookupLicenseResult]{
		OutputState: o.OutputState,
	}
}

// Beneficiary of the license.
func (o LookupLicenseResultOutput) Beneficiary() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *string { return v.Beneficiary }).(pulumi.StringPtrOutput)
}

func (o LookupLicenseResultOutput) ConsumptionConfiguration() LicenseConsumptionConfigurationPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *LicenseConsumptionConfiguration { return v.ConsumptionConfiguration }).(LicenseConsumptionConfigurationPtrOutput)
}

func (o LookupLicenseResultOutput) Entitlements() LicenseEntitlementArrayOutput {
	return o.ApplyT(func(v LookupLicenseResult) []LicenseEntitlement { return v.Entitlements }).(LicenseEntitlementArrayOutput)
}

// Home region for the created license.
func (o LookupLicenseResultOutput) HomeRegion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *string { return v.HomeRegion }).(pulumi.StringPtrOutput)
}

func (o LookupLicenseResultOutput) Issuer() LicenseIssuerDataPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *LicenseIssuerData { return v.Issuer }).(LicenseIssuerDataPtrOutput)
}

// Amazon Resource Name is a unique name for each resource.
func (o LookupLicenseResultOutput) LicenseArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *string { return v.LicenseArn }).(pulumi.StringPtrOutput)
}

func (o LookupLicenseResultOutput) LicenseMetadata() LicenseMetadataArrayOutput {
	return o.ApplyT(func(v LookupLicenseResult) []LicenseMetadata { return v.LicenseMetadata }).(LicenseMetadataArrayOutput)
}

// Name for the created license.
func (o LookupLicenseResultOutput) LicenseName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *string { return v.LicenseName }).(pulumi.StringPtrOutput)
}

// Product name for the created license.
func (o LookupLicenseResultOutput) ProductName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *string { return v.ProductName }).(pulumi.StringPtrOutput)
}

// ProductSKU of the license.
func (o LookupLicenseResultOutput) ProductSku() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *string { return v.ProductSku }).(pulumi.StringPtrOutput)
}

func (o LookupLicenseResultOutput) Validity() LicenseValidityDateFormatPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *LicenseValidityDateFormat { return v.Validity }).(LicenseValidityDateFormatPtrOutput)
}

// The version of the license.
func (o LookupLicenseResultOutput) Version() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupLicenseResult) *string { return v.Version }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupLicenseResultOutput{})
}
