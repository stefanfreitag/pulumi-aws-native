// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Glue::Partition
 *
 * @deprecated Partition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Partition extends pulumi.CustomResource {
    /**
     * Get an existing Partition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Partition {
        pulumi.log.warn("Partition is deprecated: Partition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Partition(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:glue:Partition';

    /**
     * Returns true if the given object is an instance of Partition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Partition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Partition.__pulumiType;
    }

    public readonly catalogId!: pulumi.Output<string>;
    public readonly databaseName!: pulumi.Output<string>;
    public readonly partitionInput!: pulumi.Output<outputs.glue.PartitionInput>;
    public readonly tableName!: pulumi.Output<string>;

    /**
     * Create a Partition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Partition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: PartitionArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Partition is deprecated: Partition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.catalogId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'catalogId'");
            }
            if ((!args || args.databaseName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'databaseName'");
            }
            if ((!args || args.partitionInput === undefined) && !opts.urn) {
                throw new Error("Missing required property 'partitionInput'");
            }
            if ((!args || args.tableName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tableName'");
            }
            resourceInputs["catalogId"] = args ? args.catalogId : undefined;
            resourceInputs["databaseName"] = args ? args.databaseName : undefined;
            resourceInputs["partitionInput"] = args ? args.partitionInput : undefined;
            resourceInputs["tableName"] = args ? args.tableName : undefined;
        } else {
            resourceInputs["catalogId"] = undefined /*out*/;
            resourceInputs["databaseName"] = undefined /*out*/;
            resourceInputs["partitionInput"] = undefined /*out*/;
            resourceInputs["tableName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["catalogId", "databaseName", "tableName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(Partition.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Partition resource.
 */
export interface PartitionArgs {
    catalogId: pulumi.Input<string>;
    databaseName: pulumi.Input<string>;
    partitionInput: pulumi.Input<inputs.glue.PartitionInputArgs>;
    tableName: pulumi.Input<string>;
}
