// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package networkmanager

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The AWS::NetworkManager::Site type describes a site.
func LookupSite(ctx *pulumi.Context, args *LookupSiteArgs, opts ...pulumi.InvokeOption) (*LookupSiteResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSiteResult
	err := ctx.Invoke("aws-native:networkmanager:getSite", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSiteArgs struct {
	// The ID of the global network.
	GlobalNetworkId string `pulumi:"globalNetworkId"`
	// The ID of the site.
	SiteId string `pulumi:"siteId"`
}

type LookupSiteResult struct {
	// The date and time that the device was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The description of the site.
	Description *string `pulumi:"description"`
	// The location of the site.
	Location *SiteLocation `pulumi:"location"`
	// The Amazon Resource Name (ARN) of the site.
	SiteArn *string `pulumi:"siteArn"`
	// The ID of the site.
	SiteId *string `pulumi:"siteId"`
	// The state of the site.
	State *string `pulumi:"state"`
	// The tags for the site.
	Tags []SiteTag `pulumi:"tags"`
}

func LookupSiteOutput(ctx *pulumi.Context, args LookupSiteOutputArgs, opts ...pulumi.InvokeOption) LookupSiteResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSiteResult, error) {
			args := v.(LookupSiteArgs)
			r, err := LookupSite(ctx, &args, opts...)
			var s LookupSiteResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSiteResultOutput)
}

type LookupSiteOutputArgs struct {
	// The ID of the global network.
	GlobalNetworkId pulumi.StringInput `pulumi:"globalNetworkId"`
	// The ID of the site.
	SiteId pulumi.StringInput `pulumi:"siteId"`
}

func (LookupSiteOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSiteArgs)(nil)).Elem()
}

type LookupSiteResultOutput struct{ *pulumi.OutputState }

func (LookupSiteResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSiteResult)(nil)).Elem()
}

func (o LookupSiteResultOutput) ToLookupSiteResultOutput() LookupSiteResultOutput {
	return o
}

func (o LookupSiteResultOutput) ToLookupSiteResultOutputWithContext(ctx context.Context) LookupSiteResultOutput {
	return o
}

func (o LookupSiteResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSiteResult] {
	return pulumix.Output[LookupSiteResult]{
		OutputState: o.OutputState,
	}
}

// The date and time that the device was created.
func (o LookupSiteResultOutput) CreatedAt() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSiteResult) *string { return v.CreatedAt }).(pulumi.StringPtrOutput)
}

// The description of the site.
func (o LookupSiteResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSiteResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The location of the site.
func (o LookupSiteResultOutput) Location() SiteLocationPtrOutput {
	return o.ApplyT(func(v LookupSiteResult) *SiteLocation { return v.Location }).(SiteLocationPtrOutput)
}

// The Amazon Resource Name (ARN) of the site.
func (o LookupSiteResultOutput) SiteArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSiteResult) *string { return v.SiteArn }).(pulumi.StringPtrOutput)
}

// The ID of the site.
func (o LookupSiteResultOutput) SiteId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSiteResult) *string { return v.SiteId }).(pulumi.StringPtrOutput)
}

// The state of the site.
func (o LookupSiteResultOutput) State() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSiteResult) *string { return v.State }).(pulumi.StringPtrOutput)
}

// The tags for the site.
func (o LookupSiteResultOutput) Tags() SiteTagArrayOutput {
	return o.ApplyT(func(v LookupSiteResult) []SiteTag { return v.Tags }).(SiteTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSiteResultOutput{})
}
