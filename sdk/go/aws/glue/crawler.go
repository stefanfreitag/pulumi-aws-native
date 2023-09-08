// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package glue

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::Glue::Crawler
//
// Deprecated: Crawler is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Crawler struct {
	pulumi.CustomResourceState

	Classifiers                  pulumi.StringArrayOutput           `pulumi:"classifiers"`
	Configuration                pulumi.StringPtrOutput             `pulumi:"configuration"`
	CrawlerSecurityConfiguration pulumi.StringPtrOutput             `pulumi:"crawlerSecurityConfiguration"`
	DatabaseName                 pulumi.StringPtrOutput             `pulumi:"databaseName"`
	Description                  pulumi.StringPtrOutput             `pulumi:"description"`
	Name                         pulumi.StringPtrOutput             `pulumi:"name"`
	RecrawlPolicy                CrawlerRecrawlPolicyPtrOutput      `pulumi:"recrawlPolicy"`
	Role                         pulumi.StringOutput                `pulumi:"role"`
	Schedule                     CrawlerSchedulePtrOutput           `pulumi:"schedule"`
	SchemaChangePolicy           CrawlerSchemaChangePolicyPtrOutput `pulumi:"schemaChangePolicy"`
	TablePrefix                  pulumi.StringPtrOutput             `pulumi:"tablePrefix"`
	Tags                         pulumi.AnyOutput                   `pulumi:"tags"`
	Targets                      CrawlerTargetsOutput               `pulumi:"targets"`
}

// NewCrawler registers a new resource with the given unique name, arguments, and options.
func NewCrawler(ctx *pulumi.Context,
	name string, args *CrawlerArgs, opts ...pulumi.ResourceOption) (*Crawler, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Role == nil {
		return nil, errors.New("invalid value for required argument 'Role'")
	}
	if args.Targets == nil {
		return nil, errors.New("invalid value for required argument 'Targets'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"name",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Crawler
	err := ctx.RegisterResource("aws-native:glue:Crawler", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCrawler gets an existing Crawler resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCrawler(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CrawlerState, opts ...pulumi.ResourceOption) (*Crawler, error) {
	var resource Crawler
	err := ctx.ReadResource("aws-native:glue:Crawler", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Crawler resources.
type crawlerState struct {
}

type CrawlerState struct {
}

func (CrawlerState) ElementType() reflect.Type {
	return reflect.TypeOf((*crawlerState)(nil)).Elem()
}

type crawlerArgs struct {
	Classifiers                  []string                   `pulumi:"classifiers"`
	Configuration                *string                    `pulumi:"configuration"`
	CrawlerSecurityConfiguration *string                    `pulumi:"crawlerSecurityConfiguration"`
	DatabaseName                 *string                    `pulumi:"databaseName"`
	Description                  *string                    `pulumi:"description"`
	Name                         *string                    `pulumi:"name"`
	RecrawlPolicy                *CrawlerRecrawlPolicy      `pulumi:"recrawlPolicy"`
	Role                         string                     `pulumi:"role"`
	Schedule                     *CrawlerSchedule           `pulumi:"schedule"`
	SchemaChangePolicy           *CrawlerSchemaChangePolicy `pulumi:"schemaChangePolicy"`
	TablePrefix                  *string                    `pulumi:"tablePrefix"`
	Tags                         interface{}                `pulumi:"tags"`
	Targets                      CrawlerTargets             `pulumi:"targets"`
}

// The set of arguments for constructing a Crawler resource.
type CrawlerArgs struct {
	Classifiers                  pulumi.StringArrayInput
	Configuration                pulumi.StringPtrInput
	CrawlerSecurityConfiguration pulumi.StringPtrInput
	DatabaseName                 pulumi.StringPtrInput
	Description                  pulumi.StringPtrInput
	Name                         pulumi.StringPtrInput
	RecrawlPolicy                CrawlerRecrawlPolicyPtrInput
	Role                         pulumi.StringInput
	Schedule                     CrawlerSchedulePtrInput
	SchemaChangePolicy           CrawlerSchemaChangePolicyPtrInput
	TablePrefix                  pulumi.StringPtrInput
	Tags                         pulumi.Input
	Targets                      CrawlerTargetsInput
}

func (CrawlerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*crawlerArgs)(nil)).Elem()
}

type CrawlerInput interface {
	pulumi.Input

	ToCrawlerOutput() CrawlerOutput
	ToCrawlerOutputWithContext(ctx context.Context) CrawlerOutput
}

func (*Crawler) ElementType() reflect.Type {
	return reflect.TypeOf((**Crawler)(nil)).Elem()
}

func (i *Crawler) ToCrawlerOutput() CrawlerOutput {
	return i.ToCrawlerOutputWithContext(context.Background())
}

func (i *Crawler) ToCrawlerOutputWithContext(ctx context.Context) CrawlerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CrawlerOutput)
}

func (i *Crawler) ToOutput(ctx context.Context) pulumix.Output[*Crawler] {
	return pulumix.Output[*Crawler]{
		OutputState: i.ToCrawlerOutputWithContext(ctx).OutputState,
	}
}

type CrawlerOutput struct{ *pulumi.OutputState }

func (CrawlerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Crawler)(nil)).Elem()
}

func (o CrawlerOutput) ToCrawlerOutput() CrawlerOutput {
	return o
}

func (o CrawlerOutput) ToCrawlerOutputWithContext(ctx context.Context) CrawlerOutput {
	return o
}

func (o CrawlerOutput) ToOutput(ctx context.Context) pulumix.Output[*Crawler] {
	return pulumix.Output[*Crawler]{
		OutputState: o.OutputState,
	}
}

func (o CrawlerOutput) Classifiers() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringArrayOutput { return v.Classifiers }).(pulumi.StringArrayOutput)
}

func (o CrawlerOutput) Configuration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringPtrOutput { return v.Configuration }).(pulumi.StringPtrOutput)
}

func (o CrawlerOutput) CrawlerSecurityConfiguration() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringPtrOutput { return v.CrawlerSecurityConfiguration }).(pulumi.StringPtrOutput)
}

func (o CrawlerOutput) DatabaseName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringPtrOutput { return v.DatabaseName }).(pulumi.StringPtrOutput)
}

func (o CrawlerOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringPtrOutput { return v.Description }).(pulumi.StringPtrOutput)
}

func (o CrawlerOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringPtrOutput { return v.Name }).(pulumi.StringPtrOutput)
}

func (o CrawlerOutput) RecrawlPolicy() CrawlerRecrawlPolicyPtrOutput {
	return o.ApplyT(func(v *Crawler) CrawlerRecrawlPolicyPtrOutput { return v.RecrawlPolicy }).(CrawlerRecrawlPolicyPtrOutput)
}

func (o CrawlerOutput) Role() pulumi.StringOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringOutput { return v.Role }).(pulumi.StringOutput)
}

func (o CrawlerOutput) Schedule() CrawlerSchedulePtrOutput {
	return o.ApplyT(func(v *Crawler) CrawlerSchedulePtrOutput { return v.Schedule }).(CrawlerSchedulePtrOutput)
}

func (o CrawlerOutput) SchemaChangePolicy() CrawlerSchemaChangePolicyPtrOutput {
	return o.ApplyT(func(v *Crawler) CrawlerSchemaChangePolicyPtrOutput { return v.SchemaChangePolicy }).(CrawlerSchemaChangePolicyPtrOutput)
}

func (o CrawlerOutput) TablePrefix() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Crawler) pulumi.StringPtrOutput { return v.TablePrefix }).(pulumi.StringPtrOutput)
}

func (o CrawlerOutput) Tags() pulumi.AnyOutput {
	return o.ApplyT(func(v *Crawler) pulumi.AnyOutput { return v.Tags }).(pulumi.AnyOutput)
}

func (o CrawlerOutput) Targets() CrawlerTargetsOutput {
	return o.ApplyT(func(v *Crawler) CrawlerTargetsOutput { return v.Targets }).(CrawlerTargetsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CrawlerInput)(nil)).Elem(), &Crawler{})
	pulumi.RegisterOutputType(CrawlerOutput{})
}
