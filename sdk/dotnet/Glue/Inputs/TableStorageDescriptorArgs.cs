// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue.Inputs
{

    public sealed class TableStorageDescriptorArgs : global::Pulumi.ResourceArgs
    {
        [Input("bucketColumns")]
        private InputList<string>? _bucketColumns;
        public InputList<string> BucketColumns
        {
            get => _bucketColumns ?? (_bucketColumns = new InputList<string>());
            set => _bucketColumns = value;
        }

        [Input("columns")]
        private InputList<Inputs.TableColumnArgs>? _columns;
        public InputList<Inputs.TableColumnArgs> Columns
        {
            get => _columns ?? (_columns = new InputList<Inputs.TableColumnArgs>());
            set => _columns = value;
        }

        [Input("compressed")]
        public Input<bool>? Compressed { get; set; }

        [Input("inputFormat")]
        public Input<string>? InputFormat { get; set; }

        [Input("location")]
        public Input<string>? Location { get; set; }

        [Input("numberOfBuckets")]
        public Input<int>? NumberOfBuckets { get; set; }

        [Input("outputFormat")]
        public Input<string>? OutputFormat { get; set; }

        [Input("parameters")]
        public Input<object>? Parameters { get; set; }

        [Input("schemaReference")]
        public Input<Inputs.TableSchemaReferenceArgs>? SchemaReference { get; set; }

        [Input("serdeInfo")]
        public Input<Inputs.TableSerdeInfoArgs>? SerdeInfo { get; set; }

        [Input("skewedInfo")]
        public Input<Inputs.TableSkewedInfoArgs>? SkewedInfo { get; set; }

        [Input("sortColumns")]
        private InputList<Inputs.TableOrderArgs>? _sortColumns;
        public InputList<Inputs.TableOrderArgs> SortColumns
        {
            get => _sortColumns ?? (_sortColumns = new InputList<Inputs.TableOrderArgs>());
            set => _sortColumns = value;
        }

        [Input("storedAsSubDirectories")]
        public Input<bool>? StoredAsSubDirectories { get; set; }

        public TableStorageDescriptorArgs()
        {
        }
        public static new TableStorageDescriptorArgs Empty => new TableStorageDescriptorArgs();
    }
}
