// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package route53resolver

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Route53Resolver::ResolverRule
func LookupResolverRule(ctx *pulumi.Context, args *LookupResolverRuleArgs, opts ...pulumi.InvokeOption) (*LookupResolverRuleResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupResolverRuleResult
	err := ctx.Invoke("aws-native:route53resolver:getResolverRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupResolverRuleArgs struct {
	// The ID of the endpoint that the rule is associated with.
	ResolverRuleId string `pulumi:"resolverRuleId"`
}

type LookupResolverRuleResult struct {
	// The Amazon Resource Name (ARN) of the resolver rule.
	Arn *string `pulumi:"arn"`
	// DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps
	DomainName *string `pulumi:"domainName"`
	// The name for the Resolver rule
	Name *string `pulumi:"name"`
	// The ID of the endpoint that the rule is associated with.
	ResolverEndpointId *string `pulumi:"resolverEndpointId"`
	// The ID of the endpoint that the rule is associated with.
	ResolverRuleId *string `pulumi:"resolverRuleId"`
	// An array of key-value pairs to apply to this resource.
	Tags []ResolverRuleTag `pulumi:"tags"`
	// An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.
	TargetIps []ResolverRuleTargetAddress `pulumi:"targetIps"`
}

func LookupResolverRuleOutput(ctx *pulumi.Context, args LookupResolverRuleOutputArgs, opts ...pulumi.InvokeOption) LookupResolverRuleResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupResolverRuleResult, error) {
			args := v.(LookupResolverRuleArgs)
			r, err := LookupResolverRule(ctx, &args, opts...)
			var s LookupResolverRuleResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupResolverRuleResultOutput)
}

type LookupResolverRuleOutputArgs struct {
	// The ID of the endpoint that the rule is associated with.
	ResolverRuleId pulumi.StringInput `pulumi:"resolverRuleId"`
}

func (LookupResolverRuleOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResolverRuleArgs)(nil)).Elem()
}

type LookupResolverRuleResultOutput struct{ *pulumi.OutputState }

func (LookupResolverRuleResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupResolverRuleResult)(nil)).Elem()
}

func (o LookupResolverRuleResultOutput) ToLookupResolverRuleResultOutput() LookupResolverRuleResultOutput {
	return o
}

func (o LookupResolverRuleResultOutput) ToLookupResolverRuleResultOutputWithContext(ctx context.Context) LookupResolverRuleResultOutput {
	return o
}

func (o LookupResolverRuleResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupResolverRuleResult] {
	return pulumix.Output[LookupResolverRuleResult]{
		OutputState: o.OutputState,
	}
}

// The Amazon Resource Name (ARN) of the resolver rule.
func (o LookupResolverRuleResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverRuleResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// DNS queries for this domain name are forwarded to the IP addresses that are specified in TargetIps
func (o LookupResolverRuleResultOutput) DomainName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverRuleResult) *string { return v.DomainName }).(pulumi.StringPtrOutput)
}

// The name for the Resolver rule
func (o LookupResolverRuleResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverRuleResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

// The ID of the endpoint that the rule is associated with.
func (o LookupResolverRuleResultOutput) ResolverEndpointId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverRuleResult) *string { return v.ResolverEndpointId }).(pulumi.StringPtrOutput)
}

// The ID of the endpoint that the rule is associated with.
func (o LookupResolverRuleResultOutput) ResolverRuleId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupResolverRuleResult) *string { return v.ResolverRuleId }).(pulumi.StringPtrOutput)
}

// An array of key-value pairs to apply to this resource.
func (o LookupResolverRuleResultOutput) Tags() ResolverRuleTagArrayOutput {
	return o.ApplyT(func(v LookupResolverRuleResult) []ResolverRuleTag { return v.Tags }).(ResolverRuleTagArrayOutput)
}

// An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network. Specify IPv4 addresses. IPv6 is not supported.
func (o LookupResolverRuleResultOutput) TargetIps() ResolverRuleTargetAddressArrayOutput {
	return o.ApplyT(func(v LookupResolverRuleResult) []ResolverRuleTargetAddress { return v.TargetIps }).(ResolverRuleTargetAddressArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupResolverRuleResultOutput{})
}
