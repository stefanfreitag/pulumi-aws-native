// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package elasticache

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::ElastiCache::SubnetGroup
func LookupSubnetGroup(ctx *pulumi.Context, args *LookupSubnetGroupArgs, opts ...pulumi.InvokeOption) (*LookupSubnetGroupResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupSubnetGroupResult
	err := ctx.Invoke("aws-native:elasticache:getSubnetGroup", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupSubnetGroupArgs struct {
	// The name for the cache subnet group. This value is stored as a lowercase string.
	CacheSubnetGroupName string `pulumi:"cacheSubnetGroupName"`
}

type LookupSubnetGroupResult struct {
	// The description for the cache subnet group.
	Description *string `pulumi:"description"`
	// The EC2 subnet IDs for the cache subnet group.
	SubnetIds []string         `pulumi:"subnetIds"`
	Tags      []SubnetGroupTag `pulumi:"tags"`
}

func LookupSubnetGroupOutput(ctx *pulumi.Context, args LookupSubnetGroupOutputArgs, opts ...pulumi.InvokeOption) LookupSubnetGroupResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSubnetGroupResult, error) {
			args := v.(LookupSubnetGroupArgs)
			r, err := LookupSubnetGroup(ctx, &args, opts...)
			var s LookupSubnetGroupResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSubnetGroupResultOutput)
}

type LookupSubnetGroupOutputArgs struct {
	// The name for the cache subnet group. This value is stored as a lowercase string.
	CacheSubnetGroupName pulumi.StringInput `pulumi:"cacheSubnetGroupName"`
}

func (LookupSubnetGroupOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSubnetGroupArgs)(nil)).Elem()
}

type LookupSubnetGroupResultOutput struct{ *pulumi.OutputState }

func (LookupSubnetGroupResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSubnetGroupResult)(nil)).Elem()
}

func (o LookupSubnetGroupResultOutput) ToLookupSubnetGroupResultOutput() LookupSubnetGroupResultOutput {
	return o
}

func (o LookupSubnetGroupResultOutput) ToLookupSubnetGroupResultOutputWithContext(ctx context.Context) LookupSubnetGroupResultOutput {
	return o
}

func (o LookupSubnetGroupResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupSubnetGroupResult] {
	return pulumix.Output[LookupSubnetGroupResult]{
		OutputState: o.OutputState,
	}
}

// The description for the cache subnet group.
func (o LookupSubnetGroupResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSubnetGroupResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// The EC2 subnet IDs for the cache subnet group.
func (o LookupSubnetGroupResultOutput) SubnetIds() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupSubnetGroupResult) []string { return v.SubnetIds }).(pulumi.StringArrayOutput)
}

func (o LookupSubnetGroupResultOutput) Tags() SubnetGroupTagArrayOutput {
	return o.ApplyT(func(v LookupSubnetGroupResult) []SubnetGroupTag { return v.Tags }).(SubnetGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSubnetGroupResultOutput{})
}
