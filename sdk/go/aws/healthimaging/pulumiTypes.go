// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package healthimaging

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

var _ = internal.GetEnvOrDefault

// A Map of key value pairs for Tags.
type DatastoreTags struct {
}

// DatastoreTagsInput is an input type that accepts DatastoreTagsArgs and DatastoreTagsOutput values.
// You can construct a concrete instance of `DatastoreTagsInput` via:
//
//	DatastoreTagsArgs{...}
type DatastoreTagsInput interface {
	pulumi.Input

	ToDatastoreTagsOutput() DatastoreTagsOutput
	ToDatastoreTagsOutputWithContext(context.Context) DatastoreTagsOutput
}

// A Map of key value pairs for Tags.
type DatastoreTagsArgs struct {
}

func (DatastoreTagsArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*DatastoreTags)(nil)).Elem()
}

func (i DatastoreTagsArgs) ToDatastoreTagsOutput() DatastoreTagsOutput {
	return i.ToDatastoreTagsOutputWithContext(context.Background())
}

func (i DatastoreTagsArgs) ToDatastoreTagsOutputWithContext(ctx context.Context) DatastoreTagsOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatastoreTagsOutput)
}

func (i DatastoreTagsArgs) ToOutput(ctx context.Context) pulumix.Output[DatastoreTags] {
	return pulumix.Output[DatastoreTags]{
		OutputState: i.ToDatastoreTagsOutputWithContext(ctx).OutputState,
	}
}

func (i DatastoreTagsArgs) ToDatastoreTagsPtrOutput() DatastoreTagsPtrOutput {
	return i.ToDatastoreTagsPtrOutputWithContext(context.Background())
}

func (i DatastoreTagsArgs) ToDatastoreTagsPtrOutputWithContext(ctx context.Context) DatastoreTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatastoreTagsOutput).ToDatastoreTagsPtrOutputWithContext(ctx)
}

// DatastoreTagsPtrInput is an input type that accepts DatastoreTagsArgs, DatastoreTagsPtr and DatastoreTagsPtrOutput values.
// You can construct a concrete instance of `DatastoreTagsPtrInput` via:
//
//	        DatastoreTagsArgs{...}
//
//	or:
//
//	        nil
type DatastoreTagsPtrInput interface {
	pulumi.Input

	ToDatastoreTagsPtrOutput() DatastoreTagsPtrOutput
	ToDatastoreTagsPtrOutputWithContext(context.Context) DatastoreTagsPtrOutput
}

type datastoreTagsPtrType DatastoreTagsArgs

func DatastoreTagsPtr(v *DatastoreTagsArgs) DatastoreTagsPtrInput {
	return (*datastoreTagsPtrType)(v)
}

func (*datastoreTagsPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**DatastoreTags)(nil)).Elem()
}

func (i *datastoreTagsPtrType) ToDatastoreTagsPtrOutput() DatastoreTagsPtrOutput {
	return i.ToDatastoreTagsPtrOutputWithContext(context.Background())
}

func (i *datastoreTagsPtrType) ToDatastoreTagsPtrOutputWithContext(ctx context.Context) DatastoreTagsPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DatastoreTagsPtrOutput)
}

func (i *datastoreTagsPtrType) ToOutput(ctx context.Context) pulumix.Output[*DatastoreTags] {
	return pulumix.Output[*DatastoreTags]{
		OutputState: i.ToDatastoreTagsPtrOutputWithContext(ctx).OutputState,
	}
}

// A Map of key value pairs for Tags.
type DatastoreTagsOutput struct{ *pulumi.OutputState }

func (DatastoreTagsOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*DatastoreTags)(nil)).Elem()
}

func (o DatastoreTagsOutput) ToDatastoreTagsOutput() DatastoreTagsOutput {
	return o
}

func (o DatastoreTagsOutput) ToDatastoreTagsOutputWithContext(ctx context.Context) DatastoreTagsOutput {
	return o
}

func (o DatastoreTagsOutput) ToDatastoreTagsPtrOutput() DatastoreTagsPtrOutput {
	return o.ToDatastoreTagsPtrOutputWithContext(context.Background())
}

func (o DatastoreTagsOutput) ToDatastoreTagsPtrOutputWithContext(ctx context.Context) DatastoreTagsPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v DatastoreTags) *DatastoreTags {
		return &v
	}).(DatastoreTagsPtrOutput)
}

func (o DatastoreTagsOutput) ToOutput(ctx context.Context) pulumix.Output[DatastoreTags] {
	return pulumix.Output[DatastoreTags]{
		OutputState: o.OutputState,
	}
}

type DatastoreTagsPtrOutput struct{ *pulumi.OutputState }

func (DatastoreTagsPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**DatastoreTags)(nil)).Elem()
}

func (o DatastoreTagsPtrOutput) ToDatastoreTagsPtrOutput() DatastoreTagsPtrOutput {
	return o
}

func (o DatastoreTagsPtrOutput) ToDatastoreTagsPtrOutputWithContext(ctx context.Context) DatastoreTagsPtrOutput {
	return o
}

func (o DatastoreTagsPtrOutput) ToOutput(ctx context.Context) pulumix.Output[*DatastoreTags] {
	return pulumix.Output[*DatastoreTags]{
		OutputState: o.OutputState,
	}
}

func (o DatastoreTagsPtrOutput) Elem() DatastoreTagsOutput {
	return o.ApplyT(func(v *DatastoreTags) DatastoreTags {
		if v != nil {
			return *v
		}
		var ret DatastoreTags
		return ret
	}).(DatastoreTagsOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DatastoreTagsInput)(nil)).Elem(), DatastoreTagsArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*DatastoreTagsPtrInput)(nil)).Elem(), DatastoreTagsArgs{})
	pulumi.RegisterOutputType(DatastoreTagsOutput{})
	pulumi.RegisterOutputType(DatastoreTagsPtrOutput{})
}
