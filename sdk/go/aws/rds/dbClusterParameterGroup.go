// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package rds

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The AWS::RDS::DBClusterParameterGroup resource creates a new Amazon RDS DB cluster parameter group. For more information, see Managing an Amazon Aurora DB Cluster in the Amazon Aurora User Guide.
type DbClusterParameterGroup struct {
	pulumi.CustomResourceState

	DbClusterParameterGroupName pulumi.StringPtrOutput `pulumi:"dbClusterParameterGroupName"`
	// A friendly description for this DB cluster parameter group.
	Description pulumi.StringOutput `pulumi:"description"`
	// The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
	Family pulumi.StringOutput `pulumi:"family"`
	// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
	Parameters pulumi.AnyOutput `pulumi:"parameters"`
	// The list of tags for the cluster parameter group.
	Tags DbClusterParameterGroupTagArrayOutput `pulumi:"tags"`
}

// NewDbClusterParameterGroup registers a new resource with the given unique name, arguments, and options.
func NewDbClusterParameterGroup(ctx *pulumi.Context,
	name string, args *DbClusterParameterGroupArgs, opts ...pulumi.ResourceOption) (*DbClusterParameterGroup, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Description == nil {
		return nil, errors.New("invalid value for required argument 'Description'")
	}
	if args.Family == nil {
		return nil, errors.New("invalid value for required argument 'Family'")
	}
	if args.Parameters == nil {
		return nil, errors.New("invalid value for required argument 'Parameters'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"dbClusterParameterGroupName",
		"description",
		"family",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource DbClusterParameterGroup
	err := ctx.RegisterResource("aws-native:rds:DbClusterParameterGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDbClusterParameterGroup gets an existing DbClusterParameterGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDbClusterParameterGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DbClusterParameterGroupState, opts ...pulumi.ResourceOption) (*DbClusterParameterGroup, error) {
	var resource DbClusterParameterGroup
	err := ctx.ReadResource("aws-native:rds:DbClusterParameterGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering DbClusterParameterGroup resources.
type dbClusterParameterGroupState struct {
}

type DbClusterParameterGroupState struct {
}

func (DbClusterParameterGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbClusterParameterGroupState)(nil)).Elem()
}

type dbClusterParameterGroupArgs struct {
	DbClusterParameterGroupName *string `pulumi:"dbClusterParameterGroupName"`
	// A friendly description for this DB cluster parameter group.
	Description string `pulumi:"description"`
	// The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
	Family string `pulumi:"family"`
	// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
	Parameters interface{} `pulumi:"parameters"`
	// The list of tags for the cluster parameter group.
	Tags []DbClusterParameterGroupTag `pulumi:"tags"`
}

// The set of arguments for constructing a DbClusterParameterGroup resource.
type DbClusterParameterGroupArgs struct {
	DbClusterParameterGroupName pulumi.StringPtrInput
	// A friendly description for this DB cluster parameter group.
	Description pulumi.StringInput
	// The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
	Family pulumi.StringInput
	// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
	Parameters pulumi.Input
	// The list of tags for the cluster parameter group.
	Tags DbClusterParameterGroupTagArrayInput
}

func (DbClusterParameterGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbClusterParameterGroupArgs)(nil)).Elem()
}

type DbClusterParameterGroupInput interface {
	pulumi.Input

	ToDbClusterParameterGroupOutput() DbClusterParameterGroupOutput
	ToDbClusterParameterGroupOutputWithContext(ctx context.Context) DbClusterParameterGroupOutput
}

func (*DbClusterParameterGroup) ElementType() reflect.Type {
	return reflect.TypeOf((**DbClusterParameterGroup)(nil)).Elem()
}

func (i *DbClusterParameterGroup) ToDbClusterParameterGroupOutput() DbClusterParameterGroupOutput {
	return i.ToDbClusterParameterGroupOutputWithContext(context.Background())
}

func (i *DbClusterParameterGroup) ToDbClusterParameterGroupOutputWithContext(ctx context.Context) DbClusterParameterGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DbClusterParameterGroupOutput)
}

type DbClusterParameterGroupOutput struct{ *pulumi.OutputState }

func (DbClusterParameterGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DbClusterParameterGroup)(nil)).Elem()
}

func (o DbClusterParameterGroupOutput) ToDbClusterParameterGroupOutput() DbClusterParameterGroupOutput {
	return o
}

func (o DbClusterParameterGroupOutput) ToDbClusterParameterGroupOutputWithContext(ctx context.Context) DbClusterParameterGroupOutput {
	return o
}

func (o DbClusterParameterGroupOutput) DbClusterParameterGroupName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *DbClusterParameterGroup) pulumi.StringPtrOutput { return v.DbClusterParameterGroupName }).(pulumi.StringPtrOutput)
}

// A friendly description for this DB cluster parameter group.
func (o DbClusterParameterGroupOutput) Description() pulumi.StringOutput {
	return o.ApplyT(func(v *DbClusterParameterGroup) pulumi.StringOutput { return v.Description }).(pulumi.StringOutput)
}

// The DB cluster parameter group family name. A DB cluster parameter group can be associated with one and only one DB cluster parameter group family, and can be applied only to a DB cluster running a DB engine and engine version compatible with that DB cluster parameter group family.
func (o DbClusterParameterGroupOutput) Family() pulumi.StringOutput {
	return o.ApplyT(func(v *DbClusterParameterGroup) pulumi.StringOutput { return v.Family }).(pulumi.StringOutput)
}

// An array of parameters to be modified. A maximum of 20 parameters can be modified in a single request.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::RDS::DBClusterParameterGroup` for more information about the expected schema for this property.
func (o DbClusterParameterGroupOutput) Parameters() pulumi.AnyOutput {
	return o.ApplyT(func(v *DbClusterParameterGroup) pulumi.AnyOutput { return v.Parameters }).(pulumi.AnyOutput)
}

// The list of tags for the cluster parameter group.
func (o DbClusterParameterGroupOutput) Tags() DbClusterParameterGroupTagArrayOutput {
	return o.ApplyT(func(v *DbClusterParameterGroup) DbClusterParameterGroupTagArrayOutput { return v.Tags }).(DbClusterParameterGroupTagArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DbClusterParameterGroupInput)(nil)).Elem(), &DbClusterParameterGroup{})
	pulumi.RegisterOutputType(DbClusterParameterGroupOutput{})
}
