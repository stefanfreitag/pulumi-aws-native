// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package shield

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// A grouping of protected resources so they can be handled as a collective. This resource grouping improves the accuracy of detection and reduces false positives.
func LookupProtectionGroup(ctx *pulumi.Context, args *LookupProtectionGroupArgs, opts ...pulumi.InvokeOption) (*LookupProtectionGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupProtectionGroupResult
	err := ctx.Invoke("aws-native:shield:getProtectionGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupProtectionGroupArgs struct {
	// The ARN (Amazon Resource Name) of the protection group.
	ProtectionGroupArn string `pulumi:"protectionGroupArn"`
}

type LookupProtectionGroupResult struct {
	// Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.
	// * Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
	// * Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
	// * Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.
	Aggregation *ProtectionGroupAggregation `pulumi:"aggregation"`
	// The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.
	Members []string `pulumi:"members"`
	// The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.
	Pattern *ProtectionGroupPattern `pulumi:"pattern"`
	// The ARN (Amazon Resource Name) of the protection group.
	ProtectionGroupArn *string `pulumi:"protectionGroupArn"`
	// The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.
	ResourceType *ProtectionGroupResourceType `pulumi:"resourceType"`
	// One or more tag key-value pairs for the Protection object.
	Tags []aws.Tag `pulumi:"tags"`
}

func LookupProtectionGroupOutput(ctx *pulumi.Context, args LookupProtectionGroupOutputArgs, opts ...pulumi.InvokeOption) LookupProtectionGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupProtectionGroupResult, error) {
			args := v.(LookupProtectionGroupArgs)
			r, err := LookupProtectionGroup(ctx, &args, opts...)
			var s LookupProtectionGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupProtectionGroupResultOutput)
}

type LookupProtectionGroupOutputArgs struct {
	// The ARN (Amazon Resource Name) of the protection group.
	ProtectionGroupArn pulumi.StringInput `pulumi:"protectionGroupArn"`
}

func (LookupProtectionGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProtectionGroupArgs)(nil)).Elem()
}

type LookupProtectionGroupResultOutput struct{ *pulumi.OutputState }

func (LookupProtectionGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupProtectionGroupResult)(nil)).Elem()
}

func (o LookupProtectionGroupResultOutput) ToLookupProtectionGroupResultOutput() LookupProtectionGroupResultOutput {
	return o
}

func (o LookupProtectionGroupResultOutput) ToLookupProtectionGroupResultOutputWithContext(ctx context.Context) LookupProtectionGroupResultOutput {
	return o
}

// Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.
// * Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
// * Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
// * Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront and origin resources for CloudFront distributions.
func (o LookupProtectionGroupResultOutput) Aggregation() ProtectionGroupAggregationPtrOutput {
	return o.ApplyT(func(v LookupProtectionGroupResult) *ProtectionGroupAggregation { return v.Aggregation }).(ProtectionGroupAggregationPtrOutput)
}

// The Amazon Resource Names (ARNs) of the resources to include in the protection group. You must set this when you set `Pattern` to `ARBITRARY` and you must not set it for any other `Pattern` setting.
func (o LookupProtectionGroupResultOutput) Members() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupProtectionGroupResult) []string { return v.Members }).(pulumi.StringArrayOutput)
}

// The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource Amazon Resource Names (ARNs), or include all resources of a specified resource type.
func (o LookupProtectionGroupResultOutput) Pattern() ProtectionGroupPatternPtrOutput {
	return o.ApplyT(func(v LookupProtectionGroupResult) *ProtectionGroupPattern { return v.Pattern }).(ProtectionGroupPatternPtrOutput)
}

// The ARN (Amazon Resource Name) of the protection group.
func (o LookupProtectionGroupResultOutput) ProtectionGroupArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupProtectionGroupResult) *string { return v.ProtectionGroupArn }).(pulumi.StringPtrOutput)
}

// The resource type to include in the protection group. All protected resources of this type are included in the protection group. Newly protected resources of this type are automatically added to the group. You must set this when you set `Pattern` to `BY_RESOURCE_TYPE` and you must not set it for any other `Pattern` setting.
func (o LookupProtectionGroupResultOutput) ResourceType() ProtectionGroupResourceTypePtrOutput {
	return o.ApplyT(func(v LookupProtectionGroupResult) *ProtectionGroupResourceType { return v.ResourceType }).(ProtectionGroupResourceTypePtrOutput)
}

// One or more tag key-value pairs for the Protection object.
func (o LookupProtectionGroupResultOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v LookupProtectionGroupResult) []aws.Tag { return v.Tags }).(aws.TagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupProtectionGroupResultOutput{})
}
