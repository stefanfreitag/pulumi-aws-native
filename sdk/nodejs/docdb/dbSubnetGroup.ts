// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::DocDB::DBSubnetGroup
 *
 * @deprecated DbSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class DbSubnetGroup extends pulumi.CustomResource {
    /**
     * Get an existing DbSubnetGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DbSubnetGroup {
        pulumi.log.warn("DbSubnetGroup is deprecated: DbSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new DbSubnetGroup(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:docdb:DbSubnetGroup';

    /**
     * Returns true if the given object is an instance of DbSubnetGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DbSubnetGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DbSubnetGroup.__pulumiType;
    }

    public readonly dbSubnetGroupDescription!: pulumi.Output<string>;
    public readonly dbSubnetGroupName!: pulumi.Output<string | undefined>;
    public readonly subnetIds!: pulumi.Output<string[]>;
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a DbSubnetGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated DbSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: DbSubnetGroupArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("DbSubnetGroup is deprecated: DbSubnetGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.dbSubnetGroupDescription === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dbSubnetGroupDescription'");
            }
            if ((!args || args.subnetIds === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subnetIds'");
            }
            resourceInputs["dbSubnetGroupDescription"] = args ? args.dbSubnetGroupDescription : undefined;
            resourceInputs["dbSubnetGroupName"] = args ? args.dbSubnetGroupName : undefined;
            resourceInputs["subnetIds"] = args ? args.subnetIds : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
        } else {
            resourceInputs["dbSubnetGroupDescription"] = undefined /*out*/;
            resourceInputs["dbSubnetGroupName"] = undefined /*out*/;
            resourceInputs["subnetIds"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["dbSubnetGroupName"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DbSubnetGroup.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DbSubnetGroup resource.
 */
export interface DbSubnetGroupArgs {
    dbSubnetGroupDescription: pulumi.Input<string>;
    dbSubnetGroupName?: pulumi.Input<string>;
    subnetIds: pulumi.Input<pulumi.Input<string>[]>;
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
